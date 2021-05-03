from chessapp import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    games = db.relationship('Game', backref='username', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', {self.image_file}')"


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(100), nullable=False, default="Tournament")
    time_control = db.Column(db.String(10))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    round = db.Column(db.Integer, nullable=True, default=0)
    result = db.Column(db.String(7), nullable=False)
    white = db.Column(db.String(45), nullable=False, default="white")
    white_rating = db.Column(db.Integer, nullable=False, default=0)
    black = db.Column(db.String(45), nullable=False, default="black")
    black_rating = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.white} {self.white_rating} - {self.black_rating} {self.black}"
