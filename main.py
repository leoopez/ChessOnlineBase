import lichess.api
from lichess.format import SINGLE_PGN
import chess.pgn
import chess.engine as engine
from io import StringIO
import os
import pandas as pd
import numpy as np


def main():
    p = os.path.join(os.path.normpath(os.getcwd() + os.sep),
                     os.path.join('stockfish_13_win_x64',
                                  os.path.join('stockfish_13_win_x64', 'stockfish_13_win_x64.exe')))
    print(p)
    user = lichess.api.user('lzzu')
    game = chess.pgn.read_game(StringIO(lichess.api.user_games('lzzu', max=1, format=SINGLE_PGN)))

    with chess.engine.SimpleEngine.popen_uci(p) as stockfish:
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