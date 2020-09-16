#!/usr/bin/node
const argv = process.argv;
if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const n = parseInt(argv[2]);
  for (let i = 0; i < n; i++) {
    let x = '';
    for (let j = 0; j < n; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
