'use strict'

;(function (){
    let innerHtml;
    const btnLichess = document.getElementById("btn-lichess-com");
    const btnChess = document.getElementById("btn-chess-com");
    const btnChess24 = document.getElementById("btn-chess24-com");
    const btnOwn = document.getElementById("btn-own");

    let parentDiv = document.querySelector(".token-modal");

    btnLichess.addEventListener('click', function (){
        console.log(this);
        parentDiv.innerHTML = `<div class="input-group mb-3">
                                  <input type="text" class="form-control url_value" value="Xj7wHcHx" aria-label="Recipient's username" aria-describedby="button-addon2">
                                  <a class="btn btn-outline-secondary nav_link" type="button" id="button-addon2" href="/">Button</a>
                                </div>`

        document.querySelector(".nav_link").addEventListener('click',   function() {
            this.href= `${document.querySelector(".url_value").value}`;
        });
    })


})()