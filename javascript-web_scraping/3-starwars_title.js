#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.
const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const data = JSON.parse(body).title;
    console.log(data);
  }
});
