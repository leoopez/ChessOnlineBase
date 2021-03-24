import lichess.api as lichess
from lichess.format import PGN
# import chess.engine
import chess.pgn
import chess.engine as engine
from io import StringIO
import numpy as np
import pandas as pd


def threshold(is_white) -> float:
    if is_white:
        u = int(getattr(game, 'headers')['WhiteElo'])
    else:
        u = int(getattr(game, 'headers')['BlackElo'])
    return 9 - (9/3200) * u


if __name__ == '__main__':

    name = 'lzzu'
    user_games = lichess.user_games(name, max=2, format=PGN)

    with engine.SimpleEngine.popen_uci("/usr/games/stockfish") as stockfish:

        data = pd.DataFrame(columns=[x for x in range(1, 51)])
        for i, user_game in enumerate(user_games):
            game = chess.pgn.read_game(StringIO(user_game))
            pawn_user_games = []

            node = game.game()

            if game.headers['Black'] == name:
                node = node.next()
            move = 0
            while not node.is_end() and move < 50:
                board = node.board()
                score = 0
                pawn = stockfish.analyse(board, engine.Limit(time=0.1))['score']
                print(pawn)
                if pawn.is_mate():
                    if pawn.turn:
                        pawn_user_games.append(1000)
                    else:
                        pawn_user_games.append(-1000)
                    break
                else:
                    if pawn.relative.cp > 500:
                        pawn_user_games.append(500)
                        break
                    elif pawn.relative.cp < -500:
                        pawn_user_games.append(-500)
                        break
                    else:
                        pawn_user_games.append(pawn.relative.cp)
                node = node.next()
                if node:
                    node = node.next()
                move += 1
                print(move)

            array = np.zeros(50)
            array[:len(pawn_user_games)] = pawn_user_games
            data.loc[i] = np.array(array)
