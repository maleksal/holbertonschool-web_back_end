export default function getStudentIdsSum(arrObj) {
  const idsSum = arrObj.reduce((sum, { id }) => sum + id, 0);
  return idsSum;
}
