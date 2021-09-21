export default function updateStudentGradeByCity(arrObj, city, newGrades) {
  return (arrObj.filter((a) => a.location === city)).map((infos) => {
    const Grades = newGrades.filter((curr) => curr.studentId === infos.id);
    if (!Grades.length) {
      return { ...infos, grade: 'N/A' };
    }
    return { ...infos, grade: Grades[0].grade };
  });
}
