import secrets, string
from flask import render_template, redirect, flash, url_for, request, current_app
from . import super
from .. import db
from .forms import CreateAdmin
from ..decorators import role_required
from ..models import Admin



def generate_admin_id():
    """
    Custom function for generating admin IDs. Made as random as possible using Python's ``secrets`` module and an iteration through the current list to ensure IDs do not clash
    """
    def randomize():
        """
        Main function that generates the IDs
        """
        alphabet = string.ascii_lowercase
        numbers = string.digits
        first = ''.join(secrets.choice(alphabet) for i in range(5))
        second = ''.join(secrets.choice(string.digits) for i in range(5))
        return '{}_{}'.format(first, second)
      
    # list of all admin  user IDs
    admins = [admin.user_id for admin in Admin.query.all()]

    id = randomize()    
    # ensure a generated ID does not exist
    while True:
        if id in admins:
            id = randomize()
            continue
        break
    
    return id


@super.route('/super_admin/dashboard')
@role_required('super')
def home():
    """
    View for home page of the super admin.
    """
    return render_template('super/home.html')


@super.route('/super_admin/create-admin', methods=['GET', 'POST'])
@role_required('super')
def create_admin():
    """
    View function for creating a new admin. Redirects to itself after creating an admin successfully. Flash message to denote a successful creation.
    """
    create_admin = CreateAdmin()
    if create_admin.validate_on_submit():
        # create admin object
        admin = Admin(acc_role = 'admin',
                    first_name = create_admin.first_name.data, 
                    middle_name = create_admin.middle_name.data, 
                    last_name = create_admin.last_name.data,
                    user_id = generate_admin_id(),
                    position = create_admin.position.data,
                    password = create_admin.password.data)
        # add to database and commit
        try:
            db.session.add(admin)
            db.session.commit()
            flash('Admin created successfully. Activated by default.', 'info')
            return redirect(url_for('.create_admin'))
        # flash a message if an error occurs
        except:
            flash('An error occured, please try again.', 'error')
    return render_template('super/create_admin.html', create_admin = create_admin)


@super.route('/super_admin/manage-admins', methods=['GET', 'POST'])
@role_required('super')
def manage_admins():
    """
    View function for managing admins. Admins are simply activated and deactivated, no deletion.
    """
    # list of all available admins
    admins = Admin.query.all()

    if request.method == 'POST':
        """
        After form is submitted(changes applied), all checked boxes are retrieved and admins whose ID's are seen are activated, else deactivated.
        """
        # list of all checked checkboxes
        ids = request.form.getlist('activated')
        # holds list of admins that were activated in form
        active_list = [Admin.query.get(id) for id in ids]

        # loop through admins and check against new list of active admins
        for admin in admins:
            # if found in new list, set active status to True
            if admin in active_list:
                admin.active_status = True
            # otherwise, set to False
            else:
                admin.active_status = False
            current_app.logger.info('{} - {}'.format(admin.first_name, admin.active_status))
            db.session.add(admin)
        db.session.commit()
        flash('Changes applied successfuly!', 'info')
        return redirect(url_for('.manage_admins'))
    return render_template('super/manage_admins.html', admins = admins)