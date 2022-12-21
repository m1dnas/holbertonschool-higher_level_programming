#!/usr/bin/node
const button = document.querySelector('#red_header');
button.addEventListener('click', () => addClass());

function addClass () {
    const element = document.querySelector('header');
    element.classList.add('red');
};