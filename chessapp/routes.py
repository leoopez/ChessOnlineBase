from flask import render_template, url_for, flash, redirect, request
from chessapp import app, db, bcrypt
from chessapp.forms import RegistrationForm, LoginForm, UpdateForm
from chessapp.database import User, Game
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime


from chessapp.scraper import GamePGN


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/ApiHttpError.html"), 404


@app.route('/')
def index():
    return render_template("index.html", current_time=datetime.utcnow())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created")
        return redirect(url_for("login"))
    return render_template("auth/register.html", title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccesful')
    return render_template("auth/login.html", title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/account')
@login_required
def account():
    image_file = url_for('static', filename="images/default.png")
    return render_template('account.html', image_file=image_file, title='Account')


@login_required
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = UpdateForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename="images/default.png")
    return render_template('profile.html', image_file=image_file, form=form)


@login_required
@app.route('/up')
def up_game():
    return render_template('upgame.html')


@login_required
@app.route('/<token>')
def url_game(token):
    gm = GamePGN(token)
    return render_template('chessboard.html', gm=gm.pgn.headers if gm else None, moves=gm.moves if gm else None, online=True)


@login_required
@app.route('/chessboard')
def chessboard():
    online = False
    return render_template('chessboard.html', online=False)
