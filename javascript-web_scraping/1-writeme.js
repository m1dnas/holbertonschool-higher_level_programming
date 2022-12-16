#!/usr/bin/node
const path = process.argv[2];
const writes = process.argv[3];
const fs = require('fs');
// método que sobrescribe el archivo, si el archivo ya existe
// fs.writeFile(path, data, options, callback)
fs.writeFile(path, writes, 'utf8', (err) => {
  if (err) console.log(err);
});
