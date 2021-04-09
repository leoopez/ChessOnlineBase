'use strict'

document.querySelector('.btn_start_analyse').addEventListener('click', function() {
    const pgn = document.querySelector('.text_pgn_game').value;
    if(!pgn){
        document.querySelector('.message_pgn_game').textContent = "Error, no input"
    }
    else{
        console.log(pgn);

    }
});