#!/usr/bin/node
const argv = process.argv;
if (!argv[2] || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const n = parseInt(argv[2]);
  let i = 0;
  while (i < n) {
    console.log('C is fun');
    i++;
  }
}
