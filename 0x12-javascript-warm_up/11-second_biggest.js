#!/usr/bin/node

/**
* You can assume all arguments can be converted to integer
* If no argument passed, print 0
* If the number of arguments is 1, print 0
*/

const argv = process.argv;
const argc = argv.length;

if (argc < 4) {
  console.log(0);
} else {
  const args = argv.slice(2);
  let numbers = args.map(Number);
  numbers = numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
}
