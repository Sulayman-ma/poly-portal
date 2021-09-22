from flask_wtf.form import FlaskForm
from wtforms.fields import SubmitField, SelectField
from wtforms.validators import DataRequired
from ..auth.forms import BaseSignUp



class CreateAdmin(BaseSignUp, FlaskForm):
    """
    The form for creating admins, available only to super admins
    """
    position = SelectField(validators=[DataRequired()], choices=['--Position--', 'Dean', 'HOD', 'Senior Lecturer', 'Lecturer II', 'Lecturer I', 'Assistant Lecturer'])
    submit = SubmitField('CREATE')