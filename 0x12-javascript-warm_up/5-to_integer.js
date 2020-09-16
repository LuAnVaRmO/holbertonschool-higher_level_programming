#!/usr/bin/node
const argv = process.argv;
if (argv[2]) {
  if (isNaN(argv[2])) {
    console.log('Not a number');
  } else {
    console.log('MY number: ' + parseInt(argv[2]));
  }
} else {
    console.log('Not a number');
  }

