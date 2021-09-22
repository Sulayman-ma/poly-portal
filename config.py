"""
Application configuration file. Classes based on development, production or testing.
"""
from os import environ



class Config:
    SECRET_KEY = environ['SECRET_KEY'] or '83sCG5nbDXXR#-+ghVPKLRh9837_$'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:illyrian00@localhost:3306/poly_portal'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


configs = {
    'dev': Development
}
