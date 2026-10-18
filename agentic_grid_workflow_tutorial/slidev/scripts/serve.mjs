import http from 'node:http'
import fs from 'node:fs'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../dist')
const port=Number(process.env.PORT||3033)
const types={'.html':'text/html','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.json':'application/json','.woff2':'font/woff2','.pdf':'application/pdf','.ipynb':'application/x-ipynb+json'}
http.createServer((req,res)=>{try{
 const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname)
 let p=path.resolve(root,'.'+pathname)
 if(!p.startsWith(root+path.sep)&&p!==root){res.writeHead(403);res.end();return}
 if(!fs.existsSync(p)||fs.statSync(p).isDirectory())p=path.join(root,'index.html')
 res.setHeader('Content-Type',types[path.extname(p)]||'application/octet-stream');fs.createReadStream(p).pipe(res)
}catch(e){res.writeHead(500);res.end('Unable to read file')}}).listen(port,'127.0.0.1',()=>console.log(`Slidev workshop: http://127.0.0.1:${port}`))
