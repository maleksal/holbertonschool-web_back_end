export default function appendToEachArrayValue(array, appendString) {
    const a_list = [];
    for (const i of array) {
        a_list.push(`${appendString}${i}`);
    }
    return a_list;
  }