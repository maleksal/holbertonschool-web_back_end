const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const p = 1245;

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.get('/students', (request, response) => {
  countStudents(process.argv[2]).then((result) => {
    response.send(`This is the list of our students\n${result.join('\n')}`);
  }).catch((error) => {
    response.send(error.message);
  });
});

app.listen(p);
module.exports = app;
