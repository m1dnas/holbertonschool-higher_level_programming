#!/usr/bin/node
const argv = require('process').argv;

let first = -1; let second = -1;
if (argv[2] == undefined || argv.length < 3) {
  console.log(0)
} else {
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] > first) {
      second = first
      first = argv[i]
    } else if (argv[i] > second && argv[i] != first) {
      second = argv[i]
    }
  }
  console.log(second)
}

