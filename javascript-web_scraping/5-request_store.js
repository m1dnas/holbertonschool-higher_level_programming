#!/usr/bin/node
//  script that gets the contents of a webpage and stores it in a file.
const url = process.argv[2];
const pathOfFile = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
      fs.writeFile(pathOfFile, body, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});
