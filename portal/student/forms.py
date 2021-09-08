from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import SubmitField, StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import InputRequired, EqualTo



class StudentBioData(FlaskForm):
    first_name = StringField('First Name: ', validators=[InputRequired()])
    last_name = StringField('Last Name: ', validators=[InputRequired()])
    department = StringField('Department: ', validators=[InputRequired()])
    reg_number = StringField('Registration Number: ', validators=[InputRequired()])
    level = StringField('Level: ', validators=[InputRequired()])
    submit = SubmitField('Save Changes')