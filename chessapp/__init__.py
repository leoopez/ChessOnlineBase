from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from chessapp.forms import LoginForm, RegistrationForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = "bJrskGqD8YDfLNqrswwe"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


from chessapp import routes
