"""Authentication view fucntions. 

All view fucntions dealing with logins, registerations and authorizing users to perform actions on the platform."""


import re
from flask import render_template, session, flash, url_for
from flask_login import login_user, logout_user
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash
from . import auth
from .. import db, lm
from ..models import Lecturer, Student, Admin, SuperAdmin
from .forms import LoginForm



@lm.user_loader
def load_user(user_id):
    """
    User loader callback function. Takes the user ID and loads the user according to the session cookie, ``acc_role``. Returns a user object based on the specified role Student, Admin, Lecturer or SuperAdmin.

    This function is also applied in the login view. Fingers crossed, let's hope it works.

    :param user_id: Primary key of the model
    """
    session.setdefault('acc_role', '')
    if session['acc_role'] == 'student':
        return Student.query.get(user_id)
    elif session['acc_role'] == 'lecturer':
        return Lecturer.query.get(user_id)
    elif session['acc_role'] == 'admin':
        return Admin.query.get(user_id)
    else:
        return SuperAdmin.query.get(user_id)


def identify_role(user_id):
    """
    Contains regex patterns to identify the model the user ID belongs to.
    """
    patterns = [
        (r'', 'lecturer'),
        (r'[a-z]{5}_[0-9]{5}', 'admin'),
        (r'[a-z]{5}_#[0-9]{5}', 'super')
    ]

    for pattern in patterns:
        # if match is found, return role string object
        if re.fullmatch(pattern[0], user_id):
            return pattern[1]
    return 'student'


@auth.route('/', methods = ['GET', 'POST'])
def login():
    """General login view for all users on the platform. Sets the account role session key based on pattern of user ID.
    """
    form = LoginForm()
    if form.validate_on_submit():
        # identify user role and set cookie
        acc_role = identify_role(user_id := form.user_id.data.strip())
        session['acc_role'] = acc_role

        # attempt to retrieve user
        user = load_user(user_id)

        # verify user existence and password
        if user is not None and check_password_hash(user.password_hash, password=form.password.data):
            # login user and redirect to appropriate blueprint
            login_user(user)
            # del session['acc_role']
            return redirect(url_for('{}.home'.format(acc_role)))
        form.password.data = ''
        flash('Incorrect user ID or pasword!', 'error')
    return render_template('auth/login.html', form = form)


@auth.route('/')
def logout():
    """
    Logout view. Function is obvious. Makes use of Flask-Login's logout_user() function to reset the session values and log user out. Redirects to login page.
    """
    logout_user()
    return redirect(url_for('.login', next = None))