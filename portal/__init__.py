"""Application Factory

App instance initialization, adding extensions and configuring app settings
all occur in this file.
"""

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_paranoid import Paranoid
from config import configs



db = SQLAlchemy()
migrate = Migrate()
paranoid = Paranoid()
lm = LoginManager()
csrf = CSRFProtect()

lm.login_view = 'auth.login'
paranoid.redirect_view = '/'
# ensure session_protection is disbaled to avoid clashing with Flask-Paranoid
lm.session_protection = None        


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
    lm.init_app(app)
    paranoid.init_app(app)
    csrf.init_app(app)

    # Blueprint registerations
    from .auth import auth
    from .student import student
    from .admin import admin
    from .super import super
    # from .lecturer import lecturer
    
    app.register_blueprint(auth)
    app.register_blueprint(student)
    app.register_blueprint(admin)
    # app.register_blueprint(lecturer)
    app.register_blueprint(super)

    # final app
    return app
