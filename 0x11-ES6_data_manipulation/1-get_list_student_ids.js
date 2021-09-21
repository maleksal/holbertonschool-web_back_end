export default function getListStudentIds(arrobj) {
  if (!Array.isArray(arrobj)) {
    return [];
  }
  return arrobj.map((x) => x.id);
}
