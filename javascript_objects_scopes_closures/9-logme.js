#!/usr/bin/node
let counter = 0;

exports.logMe = function (item) {
  if (item !== undefined) {
    console.log('%d: %s', counter, item);
    counter++;
  }
};
