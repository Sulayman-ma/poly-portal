import secrets
from os import path, environ
from werkzeug.security import generate_password_hash


base_dir = path.abspath(path.dirname(__file__))
temp_key = secrets.token_hex(16)
environ['secret_key'] = generate_password_hash(temp_key)


class Config:
    SECRET_KEY = environ['secret_key']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = 1
    SQLALCHEMY_DATABASE_URI = 'mysql://root:illyrian00@localhost:3306/poly_portal'



configs = {
    'dev': Development
}