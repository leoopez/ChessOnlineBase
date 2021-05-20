import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


def create_app():
    app_instance = Flask(__name__)
    app_instance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_instance.config['SECRET_KEY'] = "bJrskGqD8YDfLNqrswwe"
    app_instance.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    return app_instance


app = create_app()
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
moment = Moment(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from chessapp import routes
