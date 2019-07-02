from flask import Blueprint

blogs = Blueprint('blogs', __name__, static_folder='static', template_folder='templates')

from . import route
