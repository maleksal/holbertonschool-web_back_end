const express = require('express');

const app = express();
const p = 1245;

app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});

app.listen(p, () => {
  console.log(`Example app listening at http://localhost:${p}`);
});

module.exports = app;
