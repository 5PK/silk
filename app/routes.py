
from flask import jsonify, render_template
from flask import request
from flask_login import current_user, login_user, logout_user
from app.models import User, Post

from flask_misaka import markdown

from app import app, db
from app.forms import LoginForm, ThoughtForm


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        return render_template("app.html")

    else:
        return render_template("app.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('admin'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/writeThought', methods = ['GET', 'POST'])
def writeThought():
    if request.method == 'POST':

        print(request.form)

        reqTitle = request.form['title']
        reqPost = request.files['post'].read().decode("utf-8")

        post = Post(title=reqTitle, body=reqPost, user_id=1)
        db.session.add(post)
        try:
            db.session.commit()
            return jsonify({'message':'Upload Success!'})
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            return jsonify({'message':'Upload Fail!'})

    else:
        return render_template('write.html')



@app.route('/portfolio')
def portfolio():
    return render_template("thoughts.html")


@app.route('/tutorials')
def tutorials():
    return render_template("thoughts.html")


@app.route('/thoughts')
def thoughts():

    posts = Post.query.filter_by(user_id = 1)

    print(1)

    for post in posts:
        post.body = post.body.split("\n\n")[0]

    return render_template("thoughts.html", posts=posts)

@app.route('/thought')
def thought():
    
    postId = request.args.get('id')

    posts = Post.query.filter_by(id = postId)

    return render_template("thought.html", post=posts[0])



