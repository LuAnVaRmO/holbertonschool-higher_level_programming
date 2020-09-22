#!/usr/bin/node
// count number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let oc = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      oc += 1;
    }
  }
  return oc;
};
