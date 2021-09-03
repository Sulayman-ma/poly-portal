from os import path, environ


base_dir = path.abspath(path.dirname(__file__))


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(base_dir, 'dev.sqlite')
    DEBUG = 1


configs = {
    'dev': Development
}