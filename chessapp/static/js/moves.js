'use-strict';

function start(){
    const start_pos=["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR",
                     "bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP",
                     "wP", "wP", "wP", "wP"," wP", "wP", "wP", "wP",
                     "wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"];

    const start_squares=["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
                         "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
                         "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
                         "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"];

    const class_name=["black-rook", "black-knight", "black-bishop", "black-queen", "black-king", "black-bishop", "black-knight", "black-rook",
                         "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn", "black-pawn",
                         "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn", "white-pawn",
                         "white-rook", "white-knight", "white-bishop", "white-queen", "white-king", "white-bishop", "white-knight", "white-rook"];

    for(let i = 0 ;i<32 ;i++){
        let para = document.createElement("IMG");
        para.className = class_name[i];
        document.getElementById(`square-${start_squares[i]}`).appendChild(para);
    }
}


start();
