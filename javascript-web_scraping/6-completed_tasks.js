#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id.
const api_url = process.argv[2];
const request = require('request');

request(api_url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const completeTask = {};
    const data = JSON.parse(body);
    data.forEach(task => {
      if (task.completed == true) {
        if (completeTask[task.userId] != undefined) {
          completeTask[task.userId]++;
        } else {
          completeTask[task.userId] = 1;
        }
      }
    });
    console.log(completeTask);
  }
});
