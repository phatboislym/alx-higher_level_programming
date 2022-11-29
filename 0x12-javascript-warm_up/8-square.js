#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('Missing size');
} else if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  const size = Number(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let x = '';
    for (let j = 0; j < size; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
