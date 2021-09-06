from os import path, environ


base_dir = path.abspath(path.dirname(__file__))


class Config:
    SECRET_KEY = 'another random string'
    WTF_CSRF_SECRET_KEY = 'a random string'

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = 1


configs = {
    'dev': Development
}