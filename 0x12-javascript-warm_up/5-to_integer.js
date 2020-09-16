#!/usr/bin/node
const argv = process.argv;
if (isNaN(argv[2])) {
  console.log('Not a number');
} else if (Number.isInteger(argv[2])) {
  console.log('MY number: ' + parseInt(argv[2]));
} else {
  console.log('Not a number');
}
