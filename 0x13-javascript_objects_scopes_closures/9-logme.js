#!/usr/bin/node
/**
 * unction that prints the number of arguments already printed and the new argument value
 */
let count = 0;
function logMe (item) {
  console.log(`${count}: ${item}`);
  count++;
}
module.exports = { logMe };
