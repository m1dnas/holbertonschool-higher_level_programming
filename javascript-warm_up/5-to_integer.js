#!/usr/bin/node
const argv = require('process').argv;
// built-in isNaN determina si el valor es Not a Number o no
if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', argv[2]);
}
