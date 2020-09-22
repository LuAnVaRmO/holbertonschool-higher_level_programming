#!/usr/bin/node
// convert to another base
exports.converter = function (base) {
  function toBase (value) {
    return value.toString(base);
  }
  return toBase;
};
