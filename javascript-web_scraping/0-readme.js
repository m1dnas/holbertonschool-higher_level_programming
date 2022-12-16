#!/usr/bin/node
const path = process.argv[2];
// incluir módulo fs
const fs = require('fs');
// se usa el siguiente método para poder leer el archivo
// fs.readFile( filename, encoding, callback_function(err, data) )
fs.readFile(path, 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
