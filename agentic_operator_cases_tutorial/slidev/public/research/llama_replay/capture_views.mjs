// Render the selected recorded fields. No application or chat interface is simulated.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
import {createHash} from 'node:crypto';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/f00863x/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.dirname(fileURLToPath(import.meta.url));
const deck=path.resolve(root,'../..');
const manifest=JSON.parse(fs.readFileSync(path.join(root,'capture_manifest.json'),'utf8'));
const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
try{
 const page=await browser.newPage({viewport:{width:1160,height:800},deviceScaleFactor:2});
 for(const item of manifest){
  await page.goto(pathToFileURL(path.join(root,item.view)).href);
  await page.evaluate(()=>document.fonts.ready);
  const view=page.locator('.view');
  item.rendered_css_size=await view.boundingBox();
  await view.screenshot({path:path.join(deck,'images',item.file)});
  item.png_sha256=createHash('sha256').update(fs.readFileSync(path.join(deck,'images',item.file))).digest('hex');
  item.view_sha256=createHash('sha256').update(fs.readFileSync(path.join(root,item.view))).digest('hex');
 }
}finally{await browser.close()}
fs.writeFileSync(path.join(root,'capture_manifest.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify(manifest.map(x=>({file:x.file,size:x.rendered_css_size})),null,2));
