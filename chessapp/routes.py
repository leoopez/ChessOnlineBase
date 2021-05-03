from chessapp import app
from flask import render_template, url_for, flash, redirect, session
from chessapp.forms import RegistrationForm, LoginForm
from datetime import datetime


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/ApiHttpError.html"), 404


@app.route('/')
def home_page():
    return render_template("home.html", current_time=datetime.utcnow())


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        session['name'] = form.username.data
        flash(f'Account created Successfully', 'success')
        return redirect(url_for("home_page"))
    return render_template("auth/register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("home_page"))
    return render_template("auth/login.html", title='Register', form=form)


@app.route('/profile/<username>')
def game_page(username):
    return render_template("game.html")

