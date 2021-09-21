export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  }
  map.forEach((e) => {
    if (e[1] === 1) map.set(e[0], 100);
  });
  return map;
}
