import lichess.api
from lichess.format import PGN
import chess.engine
import chess.pgn

from io import StringIO
import time
import re
import itertools
import numpy as np
import pandas as pd
def Umbral(Is_white):
    Umbral = 0.0
    if Is_white:
        Umbral = int(getattr(game,'headers')['WhiteElo'])
    else:
        Umbral = int(getattr(game,'headers')['BlackElo'])
    return (9 - (9/3200)*Umbral)
        
if __name__ == '__main__':

    class Numpy_Chess_Games:
        def __init__(self, color):
            pass
    name = 'lzzu'
    user_games = lichess.api.user_games(name, max = 10, format = PGN)
    engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
    data = pd.DataFrame(columns = [x for x in range(1,51)])
    for i,user_game in enumerate(user_games):
        #String to IO
        game = chess.pgn.read_game(StringIO(user_game))
        
        pawn_user_games = []

        node = game.game()
        if game.headers['Black'] == name:
            node = node.next()
        move = 0
        while node:
            if move > 49:
                break
            board = node.board()
            score = 0
            pawn = engine.analyse(board, chess.engine.Limit(time=0.1))['score']
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
                elif pawn.relative.cp <-500: 
                    pawn_user_games.append(-500)
                    break
                else:
                    pawn_user_games.append(pawn.relative.cp)
            node = node.next()
            if node:
                node = node.next()
            move += 1
        array = np.zeros(50)
        array[:len(pawn_user_games)] = pawn_user_games
        data.loc[i] = np.array(array)

    print(data)
    engine.quit()
