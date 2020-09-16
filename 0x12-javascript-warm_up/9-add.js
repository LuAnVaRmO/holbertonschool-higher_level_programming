#!/usr/bin/node
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const argv = process.argv;
const x = parseInt(argv[2]);
const y = parseInt(argv[3]);

console.log(add(x, y));
