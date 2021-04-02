import lichess.api
from lichess.format import PGN
import chess.pgn
import chess.engine as engine
from io import StringIO
import os
import pandas as pd
import numpy as np

p = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir),
                 os.path.join('stockfish_13_win_x64',
                              os.path.join('stockfish_13_win_x64', 'stockfish_13_win_x64.exe')))
