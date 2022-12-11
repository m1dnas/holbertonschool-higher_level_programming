#!/usr/bin/node
const argv = require('process').argv;
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('X'.repeat(argv[2]));
  }
}
