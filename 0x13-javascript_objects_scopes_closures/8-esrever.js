#!/usr/bin/node
/**
 * function that returns the reversed version of a list
 */

function esrever (list) {
  const desrever = [];
  for (let i = list.length - 1; i >= 0; i--) {
    desrever.push(list[i]);
  }
  return desrever;
}
module.exports = { esrever };
