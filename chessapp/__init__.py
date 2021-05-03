from flask import Flask
from flask_bootstrap import Bootstrap
from chessapp.forms import LoginForm, RegistrationForm

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "bJrskGqD8YDfLNqrswwe"


from chessapp import routes
