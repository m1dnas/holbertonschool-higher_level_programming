#!/usr/bin/node
const argv = require('process').argv;
const x = parseInt(argv[2]);

function factorial (a) {
  let total = 1;

  if (isNaN(a) || a === 0) {
    return (1);
  }
  for (let i = 1; i <= a; i++) {
    total *= i;
  }
  return (total);
}

console.log(factorial(x));
