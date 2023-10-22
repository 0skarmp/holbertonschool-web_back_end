export default function appendToEachArrayValue(array, appendString) {
  const ls = [];
  for (let idx of array){
    ls.push(appendString + idx)
  }
  return array;
}

