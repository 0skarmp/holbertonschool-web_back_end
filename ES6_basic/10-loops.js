export default function appendToEachArrayValue(array, appendString) {
  const ls = [];
  for (const idx of array) {
    ls.push(appendString + idx);
  }
  return array;
}
