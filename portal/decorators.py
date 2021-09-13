from flask import current_app, session, flash, request
from flask_login import current_user, logout_user
from itertools import wraps



def login_required(roles = ['student']):
    """
    Custom login_required decorator based on user account role(role). Refer to models.py for account roles. Defaults to Student.

    This decorator logs the user out whenever they attempt to access protected view beyond their role.
    """
    def decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            """
            If user is not authenticated, redirect to login view and authenticate them. 
            If user is authenticated, but does not have the role to access the page, clear the session, forcefully log them out and return to login view.
            """
            if not current_user.is_authenticated():
                return current_app.login_manager.unauthorized()
            if ((current_user.acc_type not in roles) and (len(roles) == 1)):
                session['acc_role'] = ''
                flash('UNAUTHORIZED ACCESS. FORCED LOG OUT.')
                logout_user()
                return current_app.login_manager.unauthorized() 
            return func(*args, **kwargs)
        return function_wrapper
    return decorator