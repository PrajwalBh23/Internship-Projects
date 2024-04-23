const http = require('http')
const fs = require('fs')
const hostname = '127.0.0.1';
const port = 3000;
const home = fs.readFileSync('Web-dup.html')
const contact = fs.readFileSync('contact.html')
const history = fs.readFileSync('history.html')
const Login = fs.readFileSync('Login.html') 

const server = http.createServer((req, res) => {
  console.log(req.url)
  url = res.url;

  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  if(url='/'){
    res.end(home);
  }
  else if(url=='/contact'){
    res.end(home);
  }
  else{
    res.statusCode = 404;
    res.end("<h1>Hello World<\h1>");
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});