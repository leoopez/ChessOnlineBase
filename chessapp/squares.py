import chess
import chess.pgn
from chess.pgn import StringExporter

import lichess.api
from lichess.format import SINGLE_PGN

from io import StringIO


def game_pgn(url):
    return chess.pgn.read_game(
        StringIO(
            lichess.api.game(url, format=SINGLE_PGN)))


def get_moves(game):
    return game.mainline_moves().accept(StringExporter(columns=None, comments=False))


def wrinting_game():
    game = chess.pgn.Game()
    game.headers["Event"] = "Example"
    node = game.add_variation(chess.Move.from_uci("e2e4"))
    node = node.add_variation(chess.Move.from_uci("e7e5"))
    node.comment = "Comment"
