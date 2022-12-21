#!/usr/bin/node
const button = document.getElementById('add_item');
button.addEventListener('click', () => addElement());

function addElement () {
    const element = document.querySelector('.my_list');
    const li = document.createElement('li');
    li.textContent = 'Item';
// appendChild(): agrega una tag hija, en este caso a element
    element.appendChild(li);
};