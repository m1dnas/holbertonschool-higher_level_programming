#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const ApiUrl = process.argv[2];

request(ApiUrl, (err, response, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body);
    let counter = 0;
    data.results.forEach(element => {
      element.characters.forEach(character => {
        if (character.endsWith('/18/')) {
          counter++;
        }
      });
    });
    console.log(counter);
  }
});
