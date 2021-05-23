'use strict'

function myFunction() {
        let x = document.getElementById("token-lichess");
        x.classList.toggle('hidden');
        document.querySelector(".url-lichess-token").href = document.querySelector(".url-lichess-value").value;
        console.log(x.href);
}
