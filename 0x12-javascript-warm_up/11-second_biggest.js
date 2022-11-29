#!/usr/bin/node
const argv = process.argv;
const argc = (argv.length);
if (argc < 4) {
  console.log(0);
} else {
  const args = argv.slice(2);
  const numbers = args.map(x => Number(x));
  let max = Math.max(...numbers);
  numbers.splice(numbers.indexOf(max, numbers.indexOf(max)));
  max = Math.max(...numbers);
  console.log(max);
}
