import chess
import chess.pgn
import json
import lichess.api
from lichess.format import SINGLE_PGN
from lichess.api import ApiHttpError
from itertools import cycle
from collections import defaultdict
from io import StringIO


class GamePGN:
    def __init__(self, url):
        self.url = url
        self.pgn = self.game_pgn()
        self.moves = self.move_text()

    def game_pgn(self):
        try:
            return chess.pgn.read_game(
                StringIO(lichess.api.game(self.url, format=SINGLE_PGN)))
        except ApiHttpError:
            return None

    def move_text(self):
        pgn_moves = defaultdict(dict)
        board = self.pgn.board()
        color = ["w", "b"]
        for move, wt in zip(self.pgn.mainline_moves(), cycle(color)):
            pgn_moves[board.fullmove_number][wt] = {
                "fsq": move.from_square,
                "tsq": move.to_square,
                "san": board.san(move)
            }
            board.push(move)

        return json.dumps(pgn_moves)
