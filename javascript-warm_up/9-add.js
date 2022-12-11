#!/usr/bin/node
const argv = require('process').argv;
// Convierte (parsea) un argumento de tipo cadena y devuelve
// un entero de la base especificada (acá no puse la base)
// retorna 'NaN' si no devuelve el entero de la base especificada
const a = parseInt(argv[2]); const b = parseInt(argv[3]);
function add (c, d) {
  return c + d;
}
console.log(add(a, b));
