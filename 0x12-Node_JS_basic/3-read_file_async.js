const fs = require('fs');

const countStudents = (path) => {
  const promise = (res, reject) => {
    fs.readFile(path, (error, data) => {
      if (error) reject(Error('Cannot load the database'));

      if (data) {
        let fileData = data.toString().split('\n');

        fileData = fileData.slice(1, fileData.length - 1);

        console.log(`Number of students: ${fileData.length}`);

        const Classes = {};

        fileData.forEach((row) => {
          const st = row.split(',');

          if (!Classes[st[3]]) Classes[st[3]] = [];

          Classes[st[3]].push(st[0]);
        });

        for (const c in Classes) {
          if (c) {
            console.log(`Number of students in ${c}: ${Classes[c].length}. List: ${Classes[c].join(', ')}`);
          }
        }
      }

      res();
    });
  };

  return new Promise(promise);
};

module.exports = countStudents;
