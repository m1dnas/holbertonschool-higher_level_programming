#!/usr/bin/node
const button = document.querySelector('#toggle_header');
button.addEventListener('click', () => toggleClass());

// The header element must always have one class: red or green, 
// never both in the same time and never empty. 
// If the current class is red, when the user click on id toggle_header element,
// the class must be updated to green ; and the reverse.
function toggleClass () {
    const element = document.querySelector('header');
    if (element.classList.contains('red')) {
        element.classList.remove('red');
        element.classList.add('green');
    } else {
        element.classList.add('red');
        element.classList.remove('green');
    }
}