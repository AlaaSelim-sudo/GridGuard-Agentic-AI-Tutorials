const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { pathToFileURL } = require('url');
const { chromium } = require('C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');

const root = __dirname;
const manifestPath = path.join(root, 'hands_on_manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    args: ['--disable-extensions', '--disable-background-networking', '--no-first-run'],
  });
  const context = await browser.newContext({viewport: {width: 1160, height: 1000}, deviceScaleFactor: 1});
  await context.route(/^https?:\/\//, route => route.abort());
  const page = await context.newPage();
  const result = [];
  for (const item of manifest.assets.filter(x => x.kind === 'browser_capture')) {
    await page.goto(pathToFileURL(path.join(root, item.capture_page)).href, {waitUntil: 'load'});
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => {
      // Add only break opportunities: every original text character is retained.
      for (const cell of document.querySelectorAll('table.dataframe th,table.dataframe td')) {
        if (cell.childNodes.length !== 1 || cell.firstChild.nodeType !== Node.TEXT_NODE) continue;
        const original = cell.textContent;
        if (!original.includes('_')) continue;
        const fragment = document.createDocumentFragment();
        const parts = original.split('_');
        parts.forEach((part, index) => {
          fragment.append(document.createTextNode(part + (index < parts.length-1 ? '_' : '')));
          if (index < parts.length-1) fragment.append(document.createElement('wbr'));
        });
        cell.replaceChildren(fragment);
        if (cell.textContent !== original) throw new Error('Table label changed');
      }
    });
    const area = page.locator('#capture');
    const dims = await area.boundingBox();
    const checks = await page.evaluate(() => {
      const capture = document.querySelector('#capture');
      const table = document.querySelector('table.dataframe');
      const cells = table ? [...table.querySelectorAll('th,td')].filter(c=>c.getClientRects().length > 0 && getComputedStyle(c).display !== 'none') : [];
      const target = document.querySelector('.actual-output');
      return {
        capture_width: capture.offsetWidth,
        capture_scroll_width: capture.scrollWidth,
        output_text: target.innerText,
        visible_header_labels: table ? [...table.querySelectorAll('thead th')].filter(c=>getComputedStyle(c).display !== 'none').map(c=>c.innerText) : [],
        table_data_rows_total: table ? table.querySelectorAll('tbody tr').length : null,
        table_data_rows_visible: table ? [...table.querySelectorAll('tbody tr')].filter(r=>r.getClientRects().length>0).length : null,
        visible_cells: cells.length,
        overflowing_visible_cells: cells.filter(c=>c.scrollWidth > c.clientWidth + 1).map(c=>c.innerText),
      };
    });
    const outputPath = path.resolve(root, item.file);
    await area.screenshot({path: outputPath, animations:'disabled'});
    const bytes = fs.readFileSync(outputPath);
    item.image_sha256 = hash(bytes);
    item.bytes = bytes.length;
    item.dimensions_px = [Math.ceil(dims.width), Math.ceil(dims.height)];
    item.browser = await browser.version();
    item.viewport_px = [1160,1000];
    item.device_scale_factor = 1;
    item.capture_checks = checks;
    result.push({id:item.id,dimensions:item.dimensions_px,overflowing_cells:checks.overflowing_visible_cells,visible_headers:checks.visible_header_labels});
  }
  // Check the full review artifact displays all notebook cells and the original images.
  await page.goto(pathToFileURL(path.join(root,'index.html')).href, {waitUntil:'load'});
  manifest.review_page.browser_checks = await page.evaluate(() => ({
    cells: document.querySelectorAll('article.cell').length,
    tables: document.querySelectorAll('table.dataframe').length,
    original_plot_outputs: document.querySelectorAll('img.plot').length,
    plots_loaded: [...document.querySelectorAll('img.plot')].every(i=>i.complete && i.naturalWidth>0),
    page_heading: document.querySelector('h1').innerText,
  }));
  fs.writeFileSync(manifestPath, JSON.stringify(manifest,null,2), 'utf8');
  fs.writeFileSync(path.join(root,'capture_report.json'), JSON.stringify(result,null,2), 'utf8');
  console.log(JSON.stringify({captures:result,review:manifest.review_page.browser_checks},null,2));
  await browser.close();
})().catch(error => { console.error(error); process.exit(1); });
