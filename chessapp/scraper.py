import chess
import chess.pgn
from chess.pgn import StringExporter

import lichess.api
from lichess.format import SINGLE_PGN
from lichess.api import ApiHttpError

from io import StringIO


def game_pgn(url):
    try:
        return chess.pgn.read_game(
            StringIO(lichess.api.game(url, format=SINGLE_PGN)))
    except ApiHttpError:
        return None


def move_text(game):
    return game.mainline_moves().accept(StringExporter(columns=None, comments=False))
