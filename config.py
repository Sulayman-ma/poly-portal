from os import path, environ


base_dir = path.abspath(path.dirname(__file__))


class Config:
    SECRET_KEY = 'another random string'
    WTF_CSRF_SECRET_KEY = 'a random string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = 1
    SQLALCHEMY_DATABASE_URI = 'mysql://root:illyrian00@localhost:3306/poly_portal'



configs = {
    'dev': Development
}