"""Application Factory

App instance initialization, adding extensions and configuring app settings
all occur in this file.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import configs



db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    """ Main function adding all necessities to app instance

    return: application instance    
    """
    app = Flask(__name__)

    # app configurations
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)

    # extensions initializations
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Blueprint registerations
    from .auth import auth
    from .student import student
    
    app.register_blueprint(auth)
    app.register_blueprint(student)

    # final app
    return app