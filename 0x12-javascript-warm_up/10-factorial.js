#!/usr/bin/node
function factorial (a) {
  a = parseInt(a);
  if (a === 1 || isNaN(a)) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

const argv = process.argv;
const x = parseInt(argv[2]);
console.log(factorial(x));
