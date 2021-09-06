"""Application Factory

App instance initialization, adding extensions and configuring app settings
all occur in this file.
"""

from flask import Flask
from config import configs



def create_app(config_name):
    """ Main function adding all necessities to app instance

    return: application instance    
    """
    app = Flask(__name__)

    # app configurations
    app.config.from_object(configs[config_name])
    configs[config_name].init_app(app)

    # TODO: extensions initializations

    # Blueprint registerations
    from .auth import auth
    
    app.register_blueprint(auth)

    # final app
    return app