const http = require('http');

const p = 1245;

const rListner = function listener(request, response) {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');
  response.end('Hello Holberton School!');
};

const app = http.createServer(rListner);

app.listen(p);

module.exports = app;
