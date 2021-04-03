import os


engine_path = os.path.join(os.path.normpath(os.getcwd() + os.sep),
                     os.path.join('stockfish_13_win_x64',
                                  os.path.join('stockfish_13_win_x64', 'stockfish_13_win_x64.exe')))


from chessapp.chessapp import board_analyse
from chessapp.chessplot import save_png


save_png()
