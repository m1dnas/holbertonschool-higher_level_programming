#!/usr/bin/node
const button = document.getElementById('update_header');
button.addEventListener('click', () => changeText());

function changeText () {
    const element = document.querySelector('header');
    element.textContent = 'New Header!!!';
}