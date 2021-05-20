'use strict'

;(function () {
    const modal = document.querySelector('.modal-info');
    const overlay = document.querySelector('.overlay');
    const INNER = `<div class="container"><p>Lichess.com</p><input class="url_value" type="text" value="wWyJ8kQY"/>
            <a class="nav_link">OK!</a></div>`;
    let con;
    const add = function(){
        modal.classList.add('hidden');
        overlay.classList.add('hidden');
    }

    let addTokenGame = function (e){
        e.style.paddingTop = "1rem"
        con = e.innerHTML = INNER;
        document.querySelector(".nav_link").addEventListener('click',   function() {
            this.href= `${document.querySelector(".url_value").value}`;
        });
    }

    document.querySelector('.modal-close').addEventListener('click', function () {
        add();
    })

    document.querySelector('.overlay').addEventListener('click', function () {
        add();
    })

    document.addEventListener('keydown',(e) =>  {
        if(e.key === 'Escape'){
            add();
        }
    })

    document.getElementById('btn-lichess-com').addEventListener('click', function() {
        addTokenGame(this);
    });
})()
