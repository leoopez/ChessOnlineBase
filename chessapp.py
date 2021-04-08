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
import pandas as pd
import streamlit as st
from PIL import Image
from urllib.request import urlopen


ENGINE_PATH = os.path.join(os.path.normpath(os.getcwd() + os.sep),
                           os.path.join('stockfish_13_win_x64',
                                        os.path.join('stockfish_13_win_x64', 'stockfish_13_win_x64.exe')))
LICHESS_LOGO = "https://images.prismic.io/lichess/5cfd2630-2a8f-4fa9-8f78-04c2d9f0e5fe_lichess-box-1024.png?auto=compress,format"

def info(pgn_game='mVrtdM0i'):
    return lichess.api.game(pgn_game)

def board_analyse(pgn_game='mVrtdM0i'):
    pgn = lichess.api.game(pgn_game, format=SINGLE_PGN)
    game = chess.pgn.read_game(StringIO(pgn))

    with chess.engine.SimpleEngine.popen_uci(ENGINE_PATH) as stockfish:
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


def winning_chance():
    centipawns_fig = plt.figure(facecolor="#f1f1f1")
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax_cp = centipawns_fig.add_axes((left, bottom, width, height), facecolor="lightgray")
    #Title
    ax_cp.set_title("How does it work?", fontsize=16, fontname = 'sans-serif', color = "#d59020")

    centipawns = np.linspace(-1000, 1000, 101)
    ax_cp.set_xticks([n for n in range(-1000, 1001, 200)])
    ax_cp.set_yticks([n for n in range(20, 101, 20)])

    ax_cp.spines['right'].set_color('none')
    ax_cp.spines['top'].set_color('none')

    ax_cp.spines['bottom'].set_position(('data', 0))
    ax_cp.spines['left'].set_position(('data', 0))

    wining_chances = 50 + 50 * (2 / (1 + np.exp(-0.004 * centipawns)) - 1)
    ax_cp.plot(centipawns, wining_chances, lw=1)
    ax_cp.grid(linestyle=':', linewidth=0.5, which="both")
    return centipawns_fig


def app(data):
    fig = plt.figure(facecolor="#f1f1f1")
    left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
    ax = fig.add_axes((left, bottom, width, height), facecolor="#e1e1e1")
    ax.axhline(0, lw=1, ls = '-.', color = "lightblue" )


    score_white = data[data.columns[0]]
    score_black = data[data.columns[1]]

    x = np.arange(len(score_white))
    ax.plot(x, score_white, lw=3 ,markerfacecolor='white', markeredgewidth=0, color = 'white', label=data.columns[0])
    x = np.arange(len(score_black))
    ax.plot(x, score_black, lw=3, markerfacecolor='black', markeredgewidth=0, color ='black', label=data.columns[1]);
    ax.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0.0, facecolor='#d59020')
    fig.subplots_adjust(right=.75)
    return fig

def app_streamlit(data):
    st.area_chart(data)


def make_DataFrame(score_white: pd.Series, score_black: pd.Series):
    df = pd.DataFrame({score_white.name: score_white, score_black.name: score_black})
    return df

if __name__ == "__main__":

    st.title('Lichess Improve')
    im = Image.open(urlopen(LICHESS_LOGO))
    st.image(im)
    st.header('Paste the PGN')
    game_input = "mVrtdM0i"
    game = st.text_area("Sequence input", game_input)
    game = info()

    white_player = game['players']['white']['user']['name']
    black_player = game['players']['black']['user']['name']

    #white, black, _,_ = board_analyse()
    with open('example.npy', 'rb') as f:
        a = np.load(f)
        b = np.load(f)

    series_white = pd.Series(a, name=game['players']['white']['user']['name'])
    series_black = pd.Series(b, name=game['players']['black']['user']['name'])

    df = make_DataFrame(series_white, series_black)

    #st.write(app(df))
    #st.write(app_streamlit(df))
    #st.write(winning_chance())
