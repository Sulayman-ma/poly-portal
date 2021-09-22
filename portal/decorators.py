import re
from flask import current_app, session, flash, request, url_for, redirect
from flask_login import current_user
from functools import wraps



def role_required(roles):
    """
    Custom role_required decorator based on user account role. Refer to models for account roles. Defaults to Student.

    This decorator logs the user out whenever they attempt to access protected view beyond their role.
    """
    def decorator(func):
        @wraps(func)
        def function_wrapper(*args, **kwargs):
            """
            This condition checks the user's roles to ensure it is specified in the roles argument provided and then just to be sure, it also checks the user's ID pattern against that of admins and super admins.
            """
            role_exists = current_user.acc_role in roles
            id_match = re.fullmatch(r'[a-z]{5}_(#)*[0-9]{5}', current_user.user_id)
            if not role_exists or not id_match:
                flash('UNAUTHORIZED ACCESS.')
                return redirect(url_for('auth.logout'))
            return func(*args, **kwargs)
        return function_wrapper
    return decorator