import { constants } from 'node:fs';
import { copyFile, lstat, mkdir, readFile, readdir, realpath, writeFile } from 'node:fs/promises';
import path from 'node:path';

const DEFAULT_REPOSITORY = 'https://github.com/AlaaSelim-sudo/GridGuard-Agentic-AI-Tutorials';

function within(root, file) {
  const relative = path.relative(root, file);
  return relative === '' || (!path.isAbsolute(relative) && relative !== '..' && !relative.startsWith(`..${path.sep}`));
}

async function stat(file) {
  try { return await lstat(file); }
  catch (error) {
    if (error.code === 'ENOENT' || error.code === 'ENOTDIR') return null;
    throw error;
  }
}

function decodeAttribute(value) {
  return value.replace(/&(?:amp|quot|apos|lt|gt|#\d+|#x[\da-f]+);/gi, entity => {
    const named = { '&amp;': '&', '&quot;': '"', '&apos;': "'", '&lt;': '<', '&gt;': '>' };
    if (named[entity.toLowerCase()]) return named[entity.toLowerCase()];
    const hex = /^&#x/i.test(entity);
    const code = Number.parseInt(entity.slice(hex ? 3 : 2, -1), hex ? 16 : 10);
    return code > 0 && code <= 0x10ffff ? String.fromCodePoint(code) : entity;
  });
}

function escapeHtml(value) {
  return value.replace(/[&<>"']/g, character => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[character]));
}

async function htmlFiles(directory) {
  const files = [];
  if (!(await stat(directory))?.isDirectory()) return files;
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await htmlFiles(file));
    else if (entry.isFile() && /\.html?$/i.test(entry.name)) files.push(file);
  }
  return files.sort();
}

async function safeParent(deckRoot, file) {
  // Refuse an existing symlink anywhere along a destination directory path.
  let current = deckRoot;
  for (const part of path.relative(deckRoot, path.dirname(file)).split(path.sep).filter(Boolean)) {
    current = path.join(current, part);
    const info = await stat(current);
    if (info && (!info.isDirectory() || info.isSymbolicLink())) throw new Error('Destination parent is not a regular directory');
  }
  await mkdir(path.dirname(file), { recursive: true });
}

/** Complete links in a deployed evidence tree without changing archived bytes.
 *
 * `copied` and `redirects` are counts of newly created files. `unresolved`
 * contains one diagnostic per missing target, with its first referring page.
 */
export async function completeEvidenceLinks(repoRoot, deckOut, repositoryUrl = DEFAULT_REPOSITORY) {
  const deckRoot = await realpath(path.resolve(deckOut));
  const workshopRoot = await realpath(path.resolve(repoRoot, 'agentic_grid_workflow_tutorial'));
  const evidenceRoot = path.join(deckRoot, 'research', 'evidence');
  const repository = repositoryUrl.replace(/\/$/, '').replace(/\.git$/, '');
  const result = { copied: 0, redirects: 0, unresolved: [] };
  const missing = new Map();
  const attributes = /\b(href|src)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+))/gi;

  async function scan(allowCreate) {
    let created = 0;
    for (const page of await htmlFiles(evidenceRoot)) {
      const html = (await readFile(page, 'utf8')).replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '');
      for (const match of html.matchAll(attributes)) {
        const attribute = match[1].toLowerCase();
        const url = decodeAttribute(match[2] ?? match[3] ?? match[4]).trim();
        if (!url || url.startsWith('/') || url.startsWith('#') || /^[a-z][a-z\d+.-]*:/i.test(url)) continue;
        let relativeUrl;
        try { relativeUrl = decodeURIComponent(url.split(/[?#]/, 1)[0]); }
        catch {
          missing.set(`${page}:${url}`, { from: path.relative(deckRoot, page).split(path.sep).join('/'), url, reason: 'Invalid URL encoding' });
          continue;
        }
        if (!relativeUrl) continue;
        let target = path.resolve(path.dirname(page), relativeUrl);
        if (relativeUrl.endsWith('/')) target = path.join(target, 'index.html');
        const targetName = path.relative(deckRoot, target).split(path.sep).join('/');
        const diagnostic = { from: path.relative(deckRoot, page).split(path.sep).join('/'), url, target: targetName };
        if (!within(deckRoot, target) || !within(evidenceRoot, target)) {
          if (!(await stat(target))) missing.set(targetName, { ...diagnostic, reason: 'Target leaves the evidence tree' });
          continue;
        }
        if (await stat(target)) { missing.delete(targetName); continue; }
        const source = path.resolve(workshopRoot, path.relative(evidenceRoot, target));
        if (!within(workshopRoot, source)) {
          missing.set(targetName, { ...diagnostic, reason: 'Canonical source leaves the workshop tree' });
          continue;
        }
        const notebook = source.replace(/\.html?$/i, '.ipynb');
        const notebookInfo = attribute === 'href' && /\.html?$/i.test(source) ? await stat(notebook) : null;
        const redirect = notebookInfo?.isFile() && !notebookInfo.isSymbolicLink();
        const sourceFile = redirect ? notebook : source;
        const sourceInfo = await stat(sourceFile);
        if (!sourceInfo?.isFile() || sourceInfo.isSymbolicLink() || !within(workshopRoot, await realpath(sourceFile))) {
          missing.set(targetName, { ...diagnostic, reason: 'Canonical file is missing or is not a contained regular file' });
          continue;
        }
        if (!allowCreate) {
          missing.set(targetName, { ...diagnostic, reason: 'Link remains missing after three completion passes' });
          continue;
        }
        try {
          await safeParent(deckRoot, target);
          if (redirect) {
            const notebookPath = path.relative(workshopRoot, notebook).split(path.sep).map(encodeURIComponent).join('/');
            const destination = escapeHtml(`${repository}/blob/main/agentic_grid_workflow_tutorial/${notebookPath}`);
            const body = '<!doctype html><meta charset="utf-8"><title>Source notebook</title>'
              + `<meta http-equiv="refresh" content="0; url=${destination}">`
              + `<link rel="canonical" href="${destination}"><p>Read the <a href="${destination}">source notebook on GitHub</a>.</p>\n`;
            await writeFile(target, body, { encoding: 'utf8', flag: 'wx' });
            result.redirects += 1;
          } else {
            await copyFile(source, target, constants.COPYFILE_EXCL);
            result.copied += 1;
          }
          created += 1;
          missing.delete(targetName);
        } catch (error) {
          if (error.code === 'EEXIST') missing.delete(targetName);
          else missing.set(targetName, { ...diagnostic, reason: error.message });
        }
      }
    }
    return created;
  }

  for (let pass = 0; pass < 3; pass += 1) {
    if (!await scan(true)) break;
  }
  await scan(false);
  result.unresolved = [...missing.values()].sort((a, b) => (a.target ?? a.url).localeCompare(b.target ?? b.url));
  return result;
}
