from werkzeug.security import check_password_hash, generate_password_hash
from .. import db



class Student(db.Model):
    # Override the default table name set by the ORM
    __tablename__ = 'students'

    # table columns
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(128), nullable = False)
    last_name = db.Column(db.String(128), nullable = False)
    reg_number = db.Column(db.String(32), nullable = False, index = True, unique = True, primary_key = True)
    department = db.Column(db.String(128), nullable = False, index = True)
    level = db.Column(db.Integer, nullable = False, index = True)
    password_hash = db.Column(db.String(128))

    @property
    def password():
        return AttributeError('ACCESS DENIED')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Student {}>'.format(self.reg_number)