#!/usr/bin/node
/**
 * function that returns the number of occurrences in a list
 */

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
