"""Transparent contextual-bandit selection of an unevaluated LLM proposal.

This module learns which bounded numerical instruction deserves a simulation
trial. It does not fine-tune an LLM, operate equipment, or certify feasibility.
Only a subsequent simulator and independent engineering gate can admit an
action. Existing tutorial controller and workflow results are not changed.

The pooled linear contextual-action model uses features phi(x, a). A separate
context block for each declared operation lets preferences depend on the state:

    phi(x, a) = [operation_mask(a) tensor context(x), vote_share(a)]
    theta = solve(A, b)
    UCB(x, a) = theta.T @ phi + alpha * sqrt(phi.T @ solve(A, phi))
    A <- A + phi @ phi.T; b <- b + reward * phi

Only the selected proposal's revealed reward is used in an update. Frozen
evaluation uses the predicted reward without the exploration bonus. This is a
one-step RL formulation (contextual bandit), not SAC, PPO, or a claim of learned
grid-control advantage. The caller must separate training and held-out cases.
"""
from copy import deepcopy
from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
from collections.abc import Mapping, Sequence

import numpy as np


SCHEMA = "contextual_response_selector_v1"
CASE_FAMILIES = ("voltage", "restoration", "cyber")
BACKENDS = ("opendss", "lindistflow3", "dc")
# All values concern awareness or an already evaluated incumbent, never the
# candidate awaiting its trial. Fixed units/scales are part of the checkpoint.
CONTEXT_SCALES = {
    "load_mean": 1.0,
    "load_span": 1.0,
    "current_margin": 1.0,
    "voltage_margin": 0.05,
    "incumbent_cost": 1.0,
    "remaining_budget": 2.0,
}
CONTEXT_FIELDS = frozenset(("case_family", "planning_backend", *CONTEXT_SCALES))


def _number(value, label):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, float, np.integer, np.floating)):
        raise ValueError(f"{label} must be a finite real number")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{label} must be finite")
    return result


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be nonempty text")
    return value


def _json(value):
    """Require ordinary, finite JSON; do not coerce arbitrary Python objects."""
    def normalize(item):
        if isinstance(item, dict):
            if any(not isinstance(key, str) for key in item):
                raise ValueError("JSON object keys must be strings")
            return {key: normalize(val) for key, val in item.items()}
        if isinstance(item, list):
            return [normalize(val) for val in item]
        # Treat 1 and 1.0, and signed zero, as the same numeric parameter.
        if isinstance(item, float) and math.isfinite(item) and item.is_integer():
            return int(item)
        return item
    try:
        encoded = json.dumps(normalize(value), sort_keys=True, separators=(",", ":"), allow_nan=False)
        return json.loads(encoded)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("A finite JSON value is required") from error


def _hash(value):
    return hashlib.sha256(json.dumps(_json(value), sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def _operation(value):
    if not isinstance(value, Mapping) or set(value) != {"tool", "parameters"}:
        raise ValueError("Each operation requires exactly tool and parameters")
    _text(value["tool"], "tool")
    if not isinstance(value["parameters"], Mapping):
        raise ValueError("Operation parameters must be a JSON object")
    # Schema validation here establishes identity, not engineering permission.
    # The catalog is supplied by numerical tools and still needs their gate.
    return _json(dict(value))


def canonicalize_responses(responses, operation_catalog):
    """Aggregate one structured vote per model over canonical operations.

    ``responses`` contains {model_id, operation_id, reason} mappings. The
    predeclared catalog maps operation IDs to {tool, parameters}. Two catalog
    aliases with identical tool/parameter JSON become one candidate. Non-finite
    catalog data raises; malformed/unavailable responses are retained in the
    returned ``rejected`` list. Duplicate model IDs invalidate *all* votes by
    that model so input ordering cannot inflate or determine its vote.

    Reasons are retained for display only and never used as reward or proof.
    Callers retain full raw LLM responses and failure journals separately.
    """
    if not isinstance(operation_catalog, Mapping) or not operation_catalog:
        raise ValueError("A nonempty, predeclared operation catalog is required")
    catalog = {_text(key, "operation_id"): _operation(value)
               for key, value in operation_catalog.items()}
    if not isinstance(responses, Sequence) or isinstance(responses, (str, bytes)):
        raise ValueError("Responses must be a sequence")
    counts = {}
    for response in responses:
        model = response.get("model_id") if isinstance(response, Mapping) else None
        if isinstance(model, str):
            counts[model] = counts.get(model, 0) + 1
    groups, rejected = {}, []
    for index, response in enumerate(responses):
        try:
            if not isinstance(response, Mapping) or set(response) != {"model_id", "operation_id", "reason"}:
                raise ValueError("Response requires exactly model_id, operation_id and reason")
            model = _text(response["model_id"], "model_id")
            key = _text(response["operation_id"], "operation_id")
            _text(response["reason"], "reason")
            if counts[model] != 1:
                raise ValueError("Duplicate model identity: all its votes are excluded")
            if key not in catalog:
                raise ValueError("Response selected an operation outside the catalog")
            operation = catalog[key]
            identifier = "op_" + _hash(operation)
            row = groups.setdefault(identifier, {"candidate_id": identifier,
                "operation": deepcopy(operation), "operation_ids": [], "responses": []})
            row["operation_ids"].append(key)
            row["responses"].append(dict(response))
        except (ValueError, KeyError, TypeError) as error:
            rejected.append({"index": index, "model_id": response.get("model_id")
                             if isinstance(response, Mapping) and isinstance(response.get("model_id"), str) else None,
                             "error": str(error)})
    valid = sum(len(row["responses"]) for row in groups.values())
    candidates = []
    for identifier in sorted(groups):
        row = groups[identifier]
        row["operation_ids"] = sorted(set(row["operation_ids"]))
        row["responses"].sort(key=lambda item: item["model_id"])
        row["vote_count"] = len(row["responses"])
        row["vote_share"] = row["vote_count"] / valid
        candidates.append(row)
    return {"candidates": candidates, "rejected": rejected,
            "total_responses": len(responses), "valid_responses": valid}


def _pool(candidates):
    if not isinstance(candidates, Sequence) or isinstance(candidates, (str, bytes)) or not candidates:
        raise ValueError("At least one canonical candidate is required")
    ids, voters = set(), set()
    validated = []
    for row in candidates:
        required = {"candidate_id", "operation", "operation_ids", "responses", "vote_count", "vote_share"}
        if not isinstance(row, Mapping) or set(row) != required:
            raise ValueError("Use the canonicalize_responses candidate schema")
        operation = _operation(row["operation"])
        identifier = "op_" + _hash(operation)
        if row["candidate_id"] != identifier or identifier in ids:
            raise ValueError("Changed or duplicate canonical operation identity")
        ids.add(identifier)
        if not isinstance(row["operation_ids"], list) or not row["operation_ids"]:
            raise ValueError("Operation aliases are required")
        if row["operation_ids"] != sorted(set(row["operation_ids"])):
            raise ValueError("Operation aliases must be unique and sorted")
        if not isinstance(row["responses"], list) or not row["responses"]:
            raise ValueError("Candidate votes are required")
        if type(row["vote_count"]) is not int or row["vote_count"] != len(row["responses"]):
            raise ValueError("Vote count is inconsistent")
        for response in row["responses"]:
            if not isinstance(response, Mapping) or set(response) != {"model_id", "operation_id", "reason"}:
                raise ValueError("Invalid candidate vote")
            model = _text(response["model_id"], "model_id")
            _text(response["reason"], "reason")
            if model in voters or response["operation_id"] not in row["operation_ids"]:
                raise ValueError("Duplicate or inconsistent voter")
            voters.add(model)
        share = _number(row["vote_share"], "vote_share")
        if not 0 < share <= 1:
            raise ValueError("Vote share must lie in (0,1]")
        validated.append(row)
    total = len(voters)
    if any(abs(row["vote_share"] - row["vote_count"] / total) > 1e-12 for row in validated):
        raise ValueError("Vote shares must use the same valid response pool")
    return sorted(validated, key=lambda row: row["candidate_id"])


def majority_select(candidates):
    """Return the most-voted canonical ID, with a stable hash-ID tie break."""
    rows = _pool(candidates)
    return min(rows, key=lambda row: (-row["vote_count"], row["candidate_id"]))["candidate_id"]


def uniform_select(candidates, rng):
    """Sample unique operations uniformly, not once per duplicate LLM vote."""
    rows = _pool(candidates)
    if not isinstance(rng, np.random.Generator):
        raise ValueError("Pass an explicit numpy.random.Generator for reproducibility")
    return rows[int(rng.integers(len(rows)))]["candidate_id"]


def context_vector(context):
    """Strict pretrial feature whitelist; extra outcome fields are rejected.

    Numerical values use the fixed scales above. Missing/non-applicable
    measurements must be handled explicitly by the study protocol; this
    function will not silently impute evidence. Provenance of a value cannot be
    inferred from its name, so the caller must provide only pretrial records.
    """
    if not isinstance(context, Mapping) or set(context) != CONTEXT_FIELDS:
        raise ValueError("Context must contain exactly the declared pretrial fields")
    if context["case_family"] not in CASE_FAMILIES or context["planning_backend"] not in BACKENDS:
        raise ValueError("Unknown case family or planning backend")
    values = {key: _number(context[key], key) for key in CONTEXT_SCALES}
    if values["load_mean"] < 0 or values["load_span"] < 0:
        raise ValueError("Load summary values must be nonnegative")
    if type(context["remaining_budget"]) is not int or not 1 <= context["remaining_budget"] <= 100:
        raise ValueError("remaining_budget must be an integer from 1 to 100")
    return np.array([1.0,
        *(float(context["case_family"] == name) for name in CASE_FAMILIES),
        *(float(context["planning_backend"] == name) for name in BACKENDS),
        *(values[key] / scale for key, scale in CONTEXT_SCALES.items())], dtype=float)


@dataclass(frozen=True)
class Selection:
    """A trial allocation, never a feasibility decision or dispatch command."""
    decision_id: int
    candidate_id: str
    operation_id: str
    predicted_reward: float
    uncertainty: float
    selection_score: float
    exploring: bool
    scores: tuple


class LinUCB:
    """Small linear contextual-action bandit with explicit train/freeze state.

    Select one proposal and call update(selection, observed_reward) exactly
    once. The selected feature vector is retained internally, so updates cannot
    replace it with post-trial features. A frozen checkpoint rejects updates.
    """
    def __init__(self, operation_ids, alpha=0.5, regularization=1.0):
        if not isinstance(operation_ids, Sequence) or isinstance(operation_ids, (str, bytes)) or not operation_ids:
            raise ValueError("A nonempty, fixed operation vocabulary is required")
        self.operation_ids = tuple(sorted(_text(key, "operation_id") for key in operation_ids))
        if len(set(self.operation_ids)) != len(self.operation_ids):
            raise ValueError("Operation vocabulary must be unique")
        self.alpha = _number(alpha, "alpha")
        self.regularization = _number(regularization, "regularization")
        if self.alpha < 0 or self.regularization <= 0:
            raise ValueError("alpha >= 0 and regularization > 0 are required")
        self.context_dimension = 1 + len(CASE_FAMILIES) + len(BACKENDS) + len(CONTEXT_SCALES)
        self.dimension = len(self.operation_ids) * self.context_dimension + 1
        self._A = self.regularization * np.eye(self.dimension)
        self._b = np.zeros(self.dimension)
        self.frozen, self.updates, self.decisions = False, 0, 0
        self._pending = None

    def _features(self, context, candidate):
        aliases = candidate["operation_ids"]
        if any(key not in self.operation_ids for key in aliases):
            raise ValueError("Proposal operation was not in the frozen feature vocabulary")
        # Physically identical instructions can carry different semantic IDs.
        # Use an equal-weight mask, rather than granting duplicate vote weight.
        mask = np.array([float(key in aliases) / len(aliases) for key in self.operation_ids])
        return np.r_[np.kron(mask, context_vector(context)), candidate["vote_share"]]

    def select(self, context, candidates):
        rows = _pool(candidates)
        context_vector(context)  # Validate before any state is changed.
        if self._pending is not None:
            raise RuntimeError("Reveal the preceding selected reward before another training decision")
        weights = np.linalg.solve(self._A, self._b)
        scores = []
        features = {}
        for row in rows:
            phi = self._features(context, row)
            variance = float(phi @ np.linalg.solve(self._A, phi))
            if not math.isfinite(variance) or variance < -1e-10:
                raise ValueError("Invalid bandit covariance")
            uncertainty = math.sqrt(max(0.0, variance))
            prediction = float(weights @ phi)
            score = prediction + (0.0 if self.frozen else self.alpha * uncertainty)
            if not math.isfinite(score):
                raise ValueError("Non-finite selection score")
            scores.append((row["candidate_id"], prediction, uncertainty, score))
            features[row["candidate_id"]] = phi
        maximum = max(score[3] for score in scores)
        # Numerical ties within 1e-12 use the canonical ID, independent of input order.
        winner = min((score for score in scores if maximum - score[3] <= 1e-12), key=lambda item: item[0])
        row = next(row for row in rows if row["candidate_id"] == winner[0])
        self.decisions += 1
        decision = Selection(self.decisions, row["candidate_id"], row["operation_ids"][0],
                             winner[1], winner[2], winner[3], not self.frozen, tuple(scores))
        if not self.frozen:
            self._pending = (decision, features[row["candidate_id"]].copy())
        return decision

    def update(self, selection, reward):
        if self.frozen:
            raise RuntimeError("Frozen evaluation rejects every reward update")
        reward = _number(reward, "reward")
        if abs(reward) > 1e6:
            raise ValueError("Reward exceeds the declared numerical bound")
        if self._pending is None or selection is not self._pending[0]:
            raise ValueError("Update requires this model's pending selection object exactly once")
        phi = self._pending[1]
        self._A += np.outer(phi, phi)
        self._b += reward * phi
        self.updates += 1
        self._pending = None

    def freeze(self):
        if self._pending is not None:
            raise RuntimeError("A pending training decision needs its selected feedback before freeze")
        self.frozen = True
        return self

    def state_dict(self):
        if self._pending is not None:
            raise RuntimeError("Checkpoint after recording the pending selected feedback")
        record = {"schema": SCHEMA, "operation_ids": list(self.operation_ids), "alpha": self.alpha,
            "regularization": self.regularization, "context_fields": sorted(CONTEXT_FIELDS),
            "context_scales": CONTEXT_SCALES, "case_families": list(CASE_FAMILIES),
            "backends": list(BACKENDS), "feature_layout": "operation_context_kronecker_then_vote_share",
            "frozen": self.frozen, "updates": self.updates, "decisions": self.decisions,
            "A": self._A.tolist(), "b": self._b.tolist()}
        record["sha256"] = _hash(record)
        return deepcopy(record)

    def save(self, path):
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(self.state_dict(), indent=2, allow_nan=False), encoding="utf-8")

    @classmethod
    def load(cls, path):
        record = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            raise ValueError("Invalid checkpoint object")
        digest = record.pop("sha256", None)
        if digest != _hash(record):
            raise ValueError("Checkpoint integrity hash mismatch")
        expected = {"schema", "operation_ids", "alpha", "regularization", "context_fields", "context_scales",
                    "case_families", "backends", "feature_layout", "frozen", "updates", "decisions", "A", "b"}
        if (set(record) != expected or record["schema"] != SCHEMA
                or record["context_fields"] != sorted(CONTEXT_FIELDS)
                or record["context_scales"] != CONTEXT_SCALES
                or record["case_families"] != list(CASE_FAMILIES)
                or record["backends"] != list(BACKENDS)
                or record["feature_layout"] != "operation_context_kronecker_then_vote_share"):
            raise ValueError("Checkpoint feature schema mismatch")
        model = cls(record["operation_ids"], record["alpha"], record["regularization"])
        a, b = np.asarray(record["A"], dtype=float), np.asarray(record["b"], dtype=float)
        if (a.shape != (model.dimension, model.dimension) or b.shape != (model.dimension,)
                or not np.isfinite(a).all() or not np.isfinite(b).all()
                or not np.allclose(a, a.T, atol=1e-12, rtol=0.0)):
            raise ValueError("Invalid checkpoint matrix shape, symmetry or finite values")
        try:
            np.linalg.cholesky(a)
        except np.linalg.LinAlgError as error:
            raise ValueError("Checkpoint covariance must be positive definite") from error
        if (type(record["frozen"]) is not bool or type(record["updates"]) is not int
                or type(record["decisions"]) is not int or record["updates"] < 0
                or record["decisions"] < record["updates"]):
            raise ValueError("Invalid checkpoint train/evaluation counters")
        model._A, model._b = a.copy(), b.copy()
        model.frozen, model.updates, model.decisions = record["frozen"], record["updates"], record["decisions"]
        return model
