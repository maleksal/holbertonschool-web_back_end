const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const p = 1245;

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  response.setHeader('Content-Type', 'text/plain');
  response.write('This is the list of our students\n');

  countStudents(process.argv[2]).then((result) => {
    response.end(result);
  }).catch((error) => {
    response.end(error.message);
  });
});

app.listen(p, () => {
  console.log(`Example app listening at http://localhost:${p}`);
});

module.exports = app;
