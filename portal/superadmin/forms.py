from flask_wtf.form import FlaskForm
from wtforms.fields import SubmitField, BooleanField
from . import superadmin
from auth.forms import BaseSignUp



class CreateAdmin(BaseSignUp, FlaskForm):
    submit = SubmitField('Create')