"""Application Factory

App instance initialization, adding extensions and configuring app settings
all occur in this file.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import configs



csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    """ Main function adding all necessities to app instance

    return: application instance    
    """
    app = Flask(__name__)

    # app configurations
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)

    # extensions initializations
    csrf.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint registerations
    from .auth import auth
    
    app.register_blueprint(auth)

    # final app
    return app