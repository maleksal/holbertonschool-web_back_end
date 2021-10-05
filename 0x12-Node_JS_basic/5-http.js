const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((request, response) => {
  if (request.url === '/') {
    response.end('Hello Holberton School!');
  }
  if (request.url === '/students') {
    countStudents(process.argv[2]).then((data) => {
      response.end(`This is the list of our students\n${data}`);
    }).catch((error) => {
      response.end(`This is the list of our students\n${error.message}`);
    });
  }
});

app.listen(1245);
module.exports = app;
