import chess
import chess.pgn
import lichess.api
import numpy as np
from lichess.format import SINGLE_PGN
from io import StringIO


def print_board(count: list):
    mat = np.array(count).reshape(8, 8)
    print(mat)


lichess_game_pgn = lichess.api.game('bDFkNAHm', format=SINGLE_PGN)
chess_game_pgn = chess.pgn.read_game(StringIO(lichess_game_pgn))
init_chess_board = chess.BaseBoard()

count = [0 for _ in range(64)]

def get_count_
for square in chess.SQUARES:
    for sq in init_chess_board.attacks(square):
        if init_chess_board.color_at(square):
            count[sq] += 1

        elif not init_chess_board.color_at(square):
            count[sq] -= 1

print_board(count)

f