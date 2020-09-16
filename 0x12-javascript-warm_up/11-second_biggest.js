#!/usr/bin/node
const argv = process.argv;
const len = argv.length;
if (!argv || len <= 3) {
  console.log('0');
} else {
  let list = [];
  list = argv.sort(function (a, b) { return b - a; });
  console.log(list[3]);
}
