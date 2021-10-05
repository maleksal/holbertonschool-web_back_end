const http = require('http');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const DATABASE = args[0];

const host = '127.0.0.1';
const p = 1245;

const app = http.createServer(async (request, response) => {
  response.statusCode = 200;
  response.setHeader('Content-Type', 'text/plain');

  const { url } = request;

  if (url === '/') response.write('Hello Holberton School!');
  if (url === '/students') {
    response.write('This is the list of our students\n');
    try {
      const allStudents = await countStudents(DATABASE);
      response.end(`${allStudents.join('\n')}`);
    } catch (error) {
      response.end(error.message);
    }
  }
  response.statusCode = 404;
  response.end();
});

app.listen(p, host, () => {
});

module.exports = app;
