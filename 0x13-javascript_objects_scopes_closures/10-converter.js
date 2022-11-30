#!/usr/bin/node
/**
 * function that converts a number from base 10 to another base passed as argument
 */

function converter (base) {
  return num => num.toString(base);
}
module.exports = { converter };
