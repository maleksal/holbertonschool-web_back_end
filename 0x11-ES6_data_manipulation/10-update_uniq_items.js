export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  } else {
    for (const element of map) {
      if (element[1] === 1) {
        map.set(element[0], 100);
      }
    }
  }
  return map;
}
