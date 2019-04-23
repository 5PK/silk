from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class ThoughtForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    #post = TextAreaField('Post', validators=[DataRequired()])
    post = FileField()
    submit = SubmitField('Upload')