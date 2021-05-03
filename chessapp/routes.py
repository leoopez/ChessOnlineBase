from chessapp import app
from flask import render_template, url_for, flash, redirect
from chessapp.forms import RegistrationForm, LoginForm


@app.errorhandler(404)
def page_not_found():
    return render_template('ApiHttpError.html'), 404


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created Successfully', 'success')
        return redirect(url_for("home_page"))
    return render_template("auth/register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("home_page"))
    return render_template("auth/login.html", title='Register', form=form)


@app.route('/<username>')
def game_page(username):
    return render_template("game.html")

