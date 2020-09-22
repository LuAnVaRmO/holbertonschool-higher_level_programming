#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const valuesJson = JSON.parse(body).results;
    let count = 0;
    for (const movie of valuesJson) {
      for (const ch of movie.characters) {
        if (ch.endsWith('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
