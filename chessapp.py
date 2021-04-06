##########################
## Libraries
##########################

import lichess.api
from lichess.format import SINGLE_PGN
import chess.pgn
import chess.engine as engine
from io import StringIO
import numpy as np
import os
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

engine_path = os.path.join(os.path.normpath(os.getcwd() + os.sep),
                           os.path.join('stockfish_13_win_x64',
                                        os.path.join('stockfish_13_win_x64', 'stockfish_13_win_x64.exe')))
def get_info(pgn_game='mVrtdM0i'):
    return lichess.api.game(pgn_game)

def board_analyse(pgn_game='mVrtdM0i'):
    pgn = lichess.api.game(pgn_game, format=SINGLE_PGN)
    game = chess.pgn.read_game(StringIO(pgn))

    with chess.engine.SimpleEngine.popen_uci(engine_path) as stockfish:
        node = game.game()

        scr_w = []
        scr_b = []
        mate_w = []
        mate_b = []

        while not node.is_end():
            board = node.board()
            info = stockfish.analyse(board, chess.engine.Limit(time=0.1))['score']
            if hasattr(info.relative, 'cp'):
                if info.turn:
                    scr_w.append(info.relative.cp)
                else:
                    scr_b.append(info.relative.cp)
            else:
                if info.turn:
                    mate_w.append(info.relative.moves)
                else:
                    mate_b.append(info.relative.moves)
            node = node.next()
    return np.array(scr_w), np.array(scr_b), np.array(mate_w), np.array(mate_b)

def app(score_white: np.ndarray, score_black: np.ndarray):
    st.line_chart(score_white)
    st.line_chart(score_black)

if __name__ == "__main__":
    game = get_info()

    st.title("""
    Lichess Improves
    """)
    st.write(game['players']['white']['user']['name'])
    st.write(game['players']['black']['user']['name'])

    #white, black, _,_ = board_analyse()
    #app(white,black)