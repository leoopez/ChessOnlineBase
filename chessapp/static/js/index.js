'use strict'

;(function () {
    const modal = document.querySelector('.modal-info');
    const overlay = document.querySelector('.overlay');
    const add = function(){
        modal.classList.add('hidden');
        overlay.classList.add('hidden');
    }
    document.querySelector('.modal-close').addEventListener('click', function () {
        add();
    })

    document.querySelector('.overlay').addEventListener('click', function () {

    })

    document.addEventListener('keydown',(e) =>  {
        if(e.key === 'Escape'){
            add();
        }
    })
})()



