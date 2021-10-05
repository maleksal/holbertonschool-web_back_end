const http = require('http');
const countStudents = require('./3-read_file_async');

const p = 1245;

const app = http.createServer(async (request, response) => {
  response.statusCode = 200;
  if (request.url === '/') response.end('Hello Holberton School!');
  else if (request.url === '/students') {
    await countStudents(process.argv[2]).then((success) => {
      const output = `This is the list of our students\n${success}`;
      response.end(output);
    }).catch((err) => {
      response.end(err.message);
    });
  }
});

app.listen(p);

module.exports = app;
