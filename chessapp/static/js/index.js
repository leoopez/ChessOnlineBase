'use strict'

;(function () {
    const INNER = `<div class="container"><p>Lichess.com</p><input class="url_value" type="text" value="wWyJ8kQY"/>
            <a class="nav_link">OK!</a></div>`;
    let con;

    let addTokenGame = function (e){
        e.style.paddingTop = "1rem"
        con = e.innerHTML = INNER;
        document.querySelector(".nav_link").addEventListener('click',   function() {
            this.href= `${document.querySelector(".url_value").value}`;
        });
    }

    document.getElementById('btn-lichess-com').addEventListener('click', function() {
        addTokenGame(this);
    });
})()
