export default function getStudentsByLocation(arrObj, city) {
  const loc = arrObj.filter((x) => x.location === city);
  return loc;
}
