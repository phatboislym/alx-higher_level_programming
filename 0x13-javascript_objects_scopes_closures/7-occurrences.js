#!/usr/bin/node
function nbOccurences (list, searchElement) {
  const size = list.length;
  let count = 0;
  for (let i = 0; i < size; i++) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
}
module.exports = { nbOccurences };
