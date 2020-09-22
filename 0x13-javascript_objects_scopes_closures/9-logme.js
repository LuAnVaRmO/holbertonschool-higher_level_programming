#!/usr/bin/node
// count and print the number of argument
let argCount = 0;
exports.logMe = function (item) {
  console.log(argCount + ': ' + item);
  argCount += 1;
};
