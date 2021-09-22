from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, EqualTo



class LoginForm(FlaskForm):
    """General Login Form"""
    user_id = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Log In')


class BaseSignUp():
    """
    Base class for all signup forms to inherit from alongside the FlaskForm class.
    """
    first_name = StringField(validators=[InputRequired()])
    middle_name = StringField()
    last_name = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), EqualTo('password2', 'Passwords must match!')])
    password2 = PasswordField()