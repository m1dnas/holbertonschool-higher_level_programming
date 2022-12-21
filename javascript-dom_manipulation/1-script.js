#!/usr/bin/node
const button = document.querySelector('#red_header');
button.addEventListener('click', () => changeColor());

function changeColor() {
    const element = document.querySelector('header');
    element.style.color = '#FF0000';
};