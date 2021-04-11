'use strict'


document.querySelector('.up').addEventListener('click', function () {
    const value = Number(document.querySelector('.slider').value);
    const max = Number(document.querySelector('.max').textContent);
    console.log(typeof value, typeof max, value, max);
    if(value !== max){
        document.querySelector('.slider').value = value+1;
        console.log("!==",value, max);
    }else{
        console.log("===",value, max);
    }
})

document.querySelector('.down').addEventListener('click', function () {
    const value = document.querySelector('.slider').value;
    console.log(typeof value, typeof 1, value, 1);
    if(value !== 1){
        document.querySelector('.slider').value = value-1;
        console.log("!==",value, 1);
    }else{
        console.log("===",value, 1);
    }
    console.log(value);
})

