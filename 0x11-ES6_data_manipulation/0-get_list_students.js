export default function getListStudents() {
  const students = [
    [1, 'Guillaume', 'San Francisco'],
    [2, 'James', 'Columbia'],
    [5, 'Serena', 'San Fransisco'],
  ];

  const result = [];

  students.forEach((student) => {
    result.push(
      {
        id: student[0],
        firstName: student[1],
        location: student[2],
      },
    );
  });

  return result;
}
