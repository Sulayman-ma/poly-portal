from flask import render_template
from flask_login import login_required
from . import student
from .forms import StudentBioData



@student.route('/home', methods = ['GET'])
@login_required
def home():
    form = StudentBioData()
    return render_template('student/home.html', form = form)