from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_babel import lazy_gettext as _l
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired(), Length(min=4, max=20) ])
    password = PasswordField(_l('Password'), validators=[DataRequired(), Length(min=4, max=20)])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired(), Length(min=4, max=20) ])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired(), Length(min=4, max=20)])
    password2 = PasswordField(_l('Reenter Password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Sign Up'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("username already exsists")
    
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError("Please provide correct email ")

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password =  PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    password2 = PasswordField('Re-enter Password', validators=[DataRequired(), Length(min=4, max=20), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
