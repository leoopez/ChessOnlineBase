'use strict'

;(function () {
    const deleteTag = function (tag) {
        let it = document.querySelector(tag);
        if (it)
            it.remove();
    }

    const createDomElement = function (piece, parent, className, colPosition, rowPosition) {
        let p = document.createElement(piece);
        p.className = className;
        p.style.gridColumn = colPosition;
        p.style.gridRow = rowPosition;
        document.querySelector(`.${parent}`).appendChild(p);
        return p;
    }

    const pieceOnClick = function (it) {
        deleteTag("SQUARE")
        let square = createDomElement('SQUARE', 'layout-chessboard', "select", it.style.gridColumn, it.style.gridRow);
    }

    function start() {

        const start_col = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8];
        const start_row = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8];

        const class_name = ["black-rook", "black-knight", "black-bishop", "black-queen", "black-king", "black-bishop", "black-knight", "black-rook", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-rook", "white-knight", "white-bishop", "white-queen", "white-king", "white-bishop", "white-knight", "white-rook"];

        for (let i = 0; i < 32; i++) {
            let p = createDomElement('PIECE', 'layout-chessboard', class_name[i], start_col[i], start_row[i]);
            p.addEventListener('click', () => {
                pieceOnClick(p);
            })
        }
    }

    const init = function () {
        start();
    }
    init();

})()




