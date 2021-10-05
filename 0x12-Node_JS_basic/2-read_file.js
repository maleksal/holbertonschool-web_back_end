const fs = require('fs');

const countStudents = (path) => {
  try {
    let file = fs.readFileSync(path, { encoding: 'utf8' }).toString().split('\n');

    file = file.slice(1, file.length - 1);

    console.log(`Number of students: ${file.length}`);

    const Classes = {};

    file.forEach((row) => {
      const line = row.split(',');

      if (!Classes[line[3]]) {
        Classes[line[3]] = [];
      }
      Classes[line[3]].push(line[0]);
    });

    for (const cls in Classes) {
      if (cls) console.log(`Number of students in ${cls}: ${Classes[cls].length}. List: ${Classes[cls].join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};
module.exports = countStudents;
