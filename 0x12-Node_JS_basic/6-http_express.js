const express = require('express');

const app = express();
const p = 1245;

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.listen(p)

module.exports = app;
