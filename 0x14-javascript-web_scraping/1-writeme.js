#!/usr/bin/node
const fs = require('fs');
const fn = process.argv[2];
const data = process.argv[3];
fs.writeFile(fn, data, (err) => {
  if (err) {
    console.log(err);
  }
});
