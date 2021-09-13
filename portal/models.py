from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from . import db



class User():
    """
    Base user class for most common attributes and methods to be used by all users on platform. Every user table must be a subclass of this class.

    User ID remains in each individual model to avoid foreign key problems.

    :property acc_role: Account types are ``Student`` for Student, ``Lecturer`` for Lecturer, ``Admin`` for Admin and ``Super`` for SuperAdmin. Session should store a key ``acc_role`` to be checked while loading a user.
    """
    # table columns
    acc_role = db.Column(db.String(10), default = 'student')
    first_name = db.Column(db.String(20), nullable = False)
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20), nullable = False)
    gender = db.Column(db.CHAR(1))
    birth_date = db.Column(db.Date)
    marital_status = db.Column(db.String(15))
    home_address = db.Column(db.String(128))
    password_hash = db.Column(db.String(256))

    @property
    def password(self):
        return AttributeError('ACCESS DENIED')

    @password.setter
    def password(self, password):
        """
        User password hash setter
        """
        self.password_hash = generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        This returns a string representation of the User showing their ID and role.
        """
        return '<User {}>[{}]'.format(self.user_id, self.acc_role)

    def __init__(self, **kwargs) -> None:
        super().__init__()

    """
    Implementing functions required by Flask-Login and a few other customs.

    Ensure to recheck get_id() if issues arise
    """
    def get_id(self):
        try:
            return str(self.user_id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def get_acc_role(self):
        return self.acc_role


class Student(User, UserMixin, db.Model):
    __tablename__ = 'student'

    # unique columns
    user_id = db.Column(db.String(20), primary_key = True)

class Admin(User, UserMixin, db.Model):
    __tablename__ = 'admin'

    # unique columns
    user_id = db.Column(db.String(20), primary_key = True)
    is_admin = db.Column(db.Boolean, default = False)
    position = db.Column(db.String(20))


class Lecturer(User, UserMixin, db.Model):
    __tablename__ = 'lecturer'

    #TODO: unique columns
    user_id = db.Column(db.String(20), primary_key = True)


class SuperAdmin(User, UserMixin, db.Model):
    __tablename__ = 'superadmin'

    user_id = db.Column(db.String(20), primary_key = True)
    position = db.Column(db.String(20))