"""Authentication view fucntions. 

All view fucntions dealing with logins, registerations and authorizing users to perform actions on the platform."""


from flask import render_template
from . import auth



@auth.route('/', methods = ['GET'])
def index():
    """Index page view function.
    
    Confirms user's login status. If false, take default action and present forms to authorize the user. Else, redirect to appropriate blueprint."""
    # TODO: Confirm user session status
    return render_template('index.html')


@auth.route('/', methods = ['POST'])
def login():
    """Login view function. 

    Works with index page and redirects to appropriate blueprint as per student or lecturer."""
    return index()


@auth.route('/', methods = ['POST'])
def sign_up():
    """Sign up view function.
    
    Works on index page as does the login() and redirects back to the index page for user to login"""
    return index()