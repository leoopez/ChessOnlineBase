import chess
import chess.pgn
import lichess.api
from lichess.format import SINGLE_PGN
from io import StringIO
import pandas as pd


def game(url):
    return chess.pgn.read_game(
        StringIO(
            lichess.api.game(url, format=SINGLE_PGN)))


def squares_points(game_url):

    df = pd.DataFrame(index=[sq for sq in chess.SQUARE_NAMES])
    node = game_url.game()
    node = node.next()
    move_num = 1

    while not node.is_end():
        values = [0 for _ in range(64)]
        board = node.board()
        for square in chess.SQUARES:
            for sq in board.attacks(square):
                if board.color_at(square):
                    values[sq] += 1
                elif not board.color_at(square):
                    values[sq] -= 1
        series = pd.Series({x: y for x, y in zip(chess.SQUARE_NAMES, values)}, name=str(move_num))
        df[series.name] = series
        node = node.next()
        move_num += 1

    return df


def wrinting_game():
    game = chess.pgn.Game()
    game.headers["Event"] = "Example"
    node = game.add_variation(chess.Move.from_uci("e2e4"))
    node = node.add_variation(chess.Move.from_uci("e7e5"))
    node.comment = "Comment"