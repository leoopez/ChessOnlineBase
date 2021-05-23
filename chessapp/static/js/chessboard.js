'use strict'

;(function () {
    const deleteTag = function (tag) {
        let it = document.querySelector(tag);
        if (it)
            it.remove();
    }

    const createGridDomElement = function (piece, parent, className, colPosition, rowPosition) {
        let p = document.createElement(piece);
        p.className = className;
        p.style.gridColumn = colPosition;
        p.style.gridRow = rowPosition;
        document.querySelector(`.${parent}`).appendChild(p);
    }

    const createDomElement = function ( tag, parent, className) {
        let p = document.createElement(tag);
        p.className = className;
        document.querySelector(`.${parent}`).appendChild(p);
    }

    function start() {
        const squares = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 ,26 ,27,
         28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
         58, 59, 60, 61, 62, 63];
        const start_col = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8];
        const start_row = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8];

        const class_name = ["black-rook", "black-knight", "black-bishop", "black-queen", "black-king", "black-bishop", "black-knight", "black-rook", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-rook", "white-knight", "white-bishop", "white-queen", "white-king", "white-bishop", "white-knight", "white-rook"];

        for(let i = 0 ; i<64; i++){
            createGridDomElement('SQUARE', 'layout-chessboard', `sq-${squares[i]}`, (i%8)+1, Math.floor((i/8))+1);
        }

        for (let i = 0; i < 32; i++) {
            createDomElement('PIECE', `sq-${squares[start_col[i]-1+(start_row[i]-1)*8]}`, class_name[i]);
        }
    }

    function traversalMovesGame(){
        let currMove;

    }

    const init = function () {
        start();
        traversalMovesGame()
    }

    init();

})()




