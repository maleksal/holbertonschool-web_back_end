export default function hasValuesFromArray(set, array) {
  for (const val of array) {
    if (!set.has(val)) {
      return false;
    }
  }
  return true;
}
