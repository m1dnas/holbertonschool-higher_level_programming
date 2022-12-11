#!/usr/bin/node
const argv = require('process').argv;

if (argv[2] === undefined || argv.length < 4) {
  console.log(0);
} else {
  let first = -1; let second = -1;
  for (let i = 2; i < argv.length; i++) {
    // el parseInt lo agregué pq me tomaba solo la primera cifra de los argumentos, entonces habían fallas si un argumento tenía más de una cifra
    if (parseInt(argv[i]) > first) {
      second = first;
      first = argv[i];
    } else if (parseInt(argv[i]) > second && parseInt(argv[i]) !== first) {
      second = argv[i];
    }
  }
  console.log(second);
}
