from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import InputRequired, EqualTo



class StudentSignUp(FlaskForm):
    department_choices = ['--Department--', 'Computer Science', 'Computer Engineering', 'Pharmacy', 'Home Economics']
    level_choices = ['--Level--', 100, 200, 300, 400, 500, 600]

    first_name = StringField(validators=[InputRequired()])
    last_name = StringField(validators=[InputRequired()])
    department = SelectField(choices=department_choices, validators=[InputRequired()])
    reg_number = StringField(validators=[InputRequired()])
    level = SelectField(choices=level_choices, validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), EqualTo('password2', 'Passwords must match!')])
    password2 = PasswordField()
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """General Login Form"""
    user_id = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Log In')