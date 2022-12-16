#!/usr/bin/node
const path = process.argv[2]; 
const request = require('request');

request(path, (err, response) => {
  if (err) console.log(err);
  else console.log('code: %d', response.statusCode);
});
