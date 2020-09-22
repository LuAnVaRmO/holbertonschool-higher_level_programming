#!/usr/bin/node
const fs = require('fs');
const fn = process.argv[2];
fs.readFile(fn, 'utf-8', function (error, content) {
  console.log(error || content);
});
