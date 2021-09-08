from flask import render_template
from flask_login import login_required
from . import student
from .forms import StudentBioData



@student.route('/profile', methods = ['GET'])
@login_required
def profile():
    form = StudentBioData()
    return render_template('student/profile.html', form = form)