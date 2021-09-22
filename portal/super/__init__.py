from flask import Blueprint

super = Blueprint('super', __name__)

from . import views, forms