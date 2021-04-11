'use strict'


document.querySelector('.up').addEventListener('click', function () {
    const value = Number(document.querySelector('.slider').value);
    const max = Number(document.querySelector('.max').textContent);
    if(value !== max){
        document.querySelector('.slider').value = value+1;
    }
})

document.querySelector('.down').addEventListener('click', function () {
    const value = document.querySelector('.slider').value;
    if(value !== 1){
        document.querySelector('.slider').value = value-1;
    }
})

