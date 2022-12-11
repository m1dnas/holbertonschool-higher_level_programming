#!/usr/bin/node
const argv = require('process').argv;
if (argv) {
  console.log(argv[2], 'is', argv[3]);
}
