from lichessapp import app
from lichessapp import squares
from flask import render_template, url_for


@app.route('/')
def home_page():
    return render_template("board.html")


@app.route('/<game_url>')
def game_page(game_url):

    info = squares.game(game_url)
    data = squares.squares_points(info)

    return render_template("game.html", game=info.headers, len=len(data.columns))
