from flask import Blueprint

main = Blueprint('main', __name__, static_folder='main_static', template_folder='main_templates')

from . import errors, route
