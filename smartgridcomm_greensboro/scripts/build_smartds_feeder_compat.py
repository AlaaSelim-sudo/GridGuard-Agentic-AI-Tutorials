"""Build non-destructive OpenDSS compatibility masters for SMART-DS feeders.

The Greensboro export uses two retired PVSystem/InvControl property names.  This
module rewrites only the affected redirected files and converts every redirect
to an absolute path, so any nested feeder can be compiled independently without
editing the source dataset.  The benchmark runner imports :func:`build_overlay`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SMARTDS_ROOT = ROOT / "SMARTDS_GSO_solar_extreme_batt_high_peak_opendss"
DEFAULT_OUTPUT_ROOT = ROOT / "generated" / "smartds_feeder_compat"

REDIRECT_RE = re.compile(r"^(\s*redirect\s+)(.+?)(\s*)$", re.IGNORECASE)
BUSCOORD_RE = re.compile(r"^(\s*buscoords\s+)(.+?)(\s*)$", re.IGNORECASE)
PROPERTY_REWRITES = (
    ("kvarlimit", "kvarMax", re.compile(r"\bkvarlimit\b", re.IGNORECASE)),
    (
        "VV_RefReactivePower",
        "RefReactivePower",
        re.compile(r"\bVV_RefReactivePower\b", re.IGNORECASE),
    ),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def clean_dss_path(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == "[" and value[-1] == "]":
        value = value[1:-1]
    return value.strip().strip('"').strip("'")


def dss_path(path: Path) -> str:
    return f"[{path.resolve().as_posix()}]"


def safe_case_stem(master: Path) -> str:
    try:
        relative = master.parent.resolve().relative_to(SMARTDS_ROOT.resolve())
        raw = "__".join(relative.parts)
    except ValueError:
        raw = master.parent.name
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("._-") or "feeder"


def build_overlay(source_master: Path, output_dir: Path | None = None) -> dict[str, Any]:
    source_master = source_master.expanduser().resolve()
    if not source_master.is_file():
        raise FileNotFoundError(source_master)
    source_dir = source_master.parent
    output_dir = (
        output_dir.expanduser().resolve()
        if output_dir is not None
        else (DEFAULT_OUTPUT_ROOT / safe_case_stem(source_master)).resolve()
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    output_master = output_dir / "Master_compat.dss"

    master_lines: list[str] = []
    patched_files: list[dict[str, Any]] = []
    source_files: list[dict[str, str]] = []
    redirect_count = 0
    for original_line in source_master.read_text(encoding="utf-8-sig").splitlines():
        redirect = REDIRECT_RE.match(original_line)
        if redirect:
            redirect_count += 1
            source_file = (source_dir / clean_dss_path(redirect.group(2))).resolve()
            if not source_file.is_file():
                raise FileNotFoundError(f"Missing SMART-DS redirect target: {source_file}")
            source_files.append({"path": str(source_file), "sha256": sha256(source_file)})
            target = source_file
            original_text = source_file.read_text(encoding="utf-8-sig")
            patched_text = original_text
            replacement_counts: dict[str, int] = {}
            for old_name, new_name, pattern in PROPERTY_REWRITES:
                patched_text, count = pattern.subn(new_name, patched_text)
                if count:
                    replacement_counts[f"{old_name}->{new_name}"] = count
            if replacement_counts:
                try:
                    relative_target = source_file.relative_to(source_dir)
                except ValueError:
                    try:
                        relative_target = source_file.relative_to(SMARTDS_ROOT.resolve())
                    except ValueError:
                        relative_target = Path(source_file.name)
                # Preserve the source-relative directory structure. Composite
                # substation masters redirect several files with identical
                # basenames (for example each child feeder's PVSystems.dss);
                # flattening those names aliases every redirect to the last
                # rewritten file and silently corrupts the compiled circuit.
                target = output_dir / "patched" / relative_target
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    patched_text + ("" if patched_text.endswith("\n") else "\n"),
                    encoding="utf-8",
                )
                patched_files.append({
                    "source": str(source_file),
                    "target": str(target),
                    "replacement_counts": replacement_counts,
                    "replacement_count": sum(replacement_counts.values()),
                    "source_sha256": sha256(source_file),
                    "patched_sha256": sha256(target),
                })
            master_lines.append(f"Redirect {dss_path(target)}")
            continue

        buscoords = BUSCOORD_RE.match(original_line)
        if buscoords:
            source_file = (source_dir / clean_dss_path(buscoords.group(2))).resolve()
            if source_file.is_file():
                master_lines.append(f"Buscoords {dss_path(source_file)}")
            else:
                master_lines.append("! Missing source Buscoords disabled: " + original_line.strip())
            continue

        normalized = original_line.strip().lower()
        if normalized == "solve" or normalized.startswith("plot "):
            master_lines.append("! Disabled by GridGuard compatibility overlay: " + original_line.strip())
            continue
        master_lines.append(original_line)

    output_master.write_text("\n".join(master_lines) + "\n", encoding="utf-8")
    unique_source_files = {
        item["path"]: item["sha256"] for item in source_files
    }
    source_tree_payload = json.dumps(
        sorted(unique_source_files.items()), separators=(",", ":")
    ).encode("utf-8")
    manifest = {
        "source_directory": str(source_dir),
        "source_master": str(source_master),
        "source_master_sha256": sha256(source_master),
        "compatibility_master": str(output_master),
        "compatibility_master_sha256": sha256(output_master),
        "redirect_count": redirect_count,
        "patched_file_count": len(patched_files),
        "replacement_count": sum(item["replacement_count"] for item in patched_files),
        "redirected_source_file_count": len(unique_source_files),
        "redirected_source_tree_sha256": hashlib.sha256(source_tree_payload).hexdigest(),
        "redirected_source_files": [
            {"path": path, "sha256": digest}
            for path, digest in sorted(unique_source_files.items())
        ],
        "transformations": [f"{old}->{new}" for old, new, _ in PROPERTY_REWRITES],
        "original_dataset_modified": False,
        "solve_command_disabled": True,
        "plot_command_disabled": True,
        "patched_files": patched_files,
    }
    manifest_path = output_dir / "compat_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    manifest["manifest"] = str(manifest_path)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a compatibility master for one nested SMART-DS feeder.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("master", type=Path, help="Source nested-feeder Master.dss")
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest = build_overlay(args.master, args.output_dir)
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
