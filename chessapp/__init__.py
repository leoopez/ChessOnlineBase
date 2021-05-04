from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
bcrypt = Bcrypt(app)
login = LoginManager(app)

app.config['SECRET_KEY'] = "bJrskGqD8YDfLNqrswwe"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


from chessapp import routes
