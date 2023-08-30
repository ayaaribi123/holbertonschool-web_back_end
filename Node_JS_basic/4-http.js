const http = require('http');

const app = http.createServer((req, res) => {
  res.statusCode = 600;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello Holberton School!');
});
module.exports = app;
