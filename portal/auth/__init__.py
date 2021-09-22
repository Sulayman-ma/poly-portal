"""Authentication blueprint"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

# importing view functions to be included in blueprint
from . import views, forms