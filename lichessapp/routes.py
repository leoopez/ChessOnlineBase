from lichessapp import app
from lichessapp import squares
from flask import render_template, url_for
from lichess.api import ApiHttpError
import json

@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/<game_url>')
def game_page(game_url):

    while True:
        try:
            info = squares.game(game_url)
            data = squares.squares_points(info)
        except ApiHttpError:
            return render_template("ApiHttpError.html")
        else:
            return render_template("game.html", game=info.headers, len=len(data.columns), dict_data=data.to_json())

