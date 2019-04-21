from flask import render_template, flash, redirect
from flask import jsonify
from flask import request

from app.models import User

from app import app
from app.forms import LoginForm

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/admin', methods=["GET","POST"])
def admin():
    if request.method == "POST":
        return render_template("app.html")
    
    else:
        return render_template("app.html")


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
                form.email.data, form.remember_me.data))
            return redirect('/admin')
        return render_template('login.html', title='Sign In', form=form)
    else:
        form = LoginForm()
        return render_template('login.html', title='Sign In', form=form)
        

@app.route('/portfolio')
def portfolio():
    return render_template("thoughts.html")


@app.route('/tutorials')
def tutorials():
    return render_template("thoughts.html")


@app.route('/thoughts')
def thoughts():
    return render_template("thoughts.html")


'''
@app.route('/login' ,methods = ['POST'])
def login():
    if request.method == 'POST':
'''
