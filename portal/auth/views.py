"""Authentication view fucntions. 

All view fucntions dealing with logins, registerations and authorizing users to perform actions on the platform."""


from flask import render_template, session, flash, url_for
from flask_login.utils import login_user
from werkzeug.utils import redirect
from datetime import timedelta
from . import auth
from .. import db, login_manager
from ..student.models import Student
from .forms import StudentSignUp, LoginForm



@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(user_id)


@auth.route('/', methods = ['GET', 'POST'])
def login():
    """Login page view function.
    
    Handles login/user authorization and redirects to appropriate blueprint. Function behaviour will be changed."""
    form = LoginForm()
    if form.validate_on_submit():
        user = Student.query.filter_by(reg_number=form.user_id.data).first()
        if user is not None and user.verify_password(form.password.data):
            # log user in and remember session for 24 hours
            login_user(user, duration=timedelta(hours=24))
            return redirect(url_for('student.profile'))
        flash('Invalid user ID or password')
    return render_template('auth/login.html', form = form)


@auth.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    """Sign up view function.
    
    Redirects user to sign up page on authentication blueprint"""
    form = StudentSignUp()
    if form.validate_on_submit():
        user = Student(first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        reg_number = form.reg_number.data,
                        department = form.department.data,
                        level = form.level.data,
                        password = form.password.data)
        db.session.add(user)
        db.session.commit()
        # save student reg number to session to keep them logged in
        session['reg_number'] = user.reg_number
        return redirect(url_for('.login'))
    return render_template('auth/signup.html', form = form)