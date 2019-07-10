from flask import Flask
from config import config
from database import db
from flask_moment import Moment
from flask_migrate import Migrate
from flask_login import LoginManager
from jinja2 import filters
from application.main import main
from application.users import users
from application.blogs import blogs
from application.help_func.jinja2_custom_filters import is_list

moment = Moment()
migrate = Migrate()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = ''


def create_app(config_name=config.get('default')):
    if not config_name:
        raise ValueError('default configuration for flask application does not exist.')
    check_config = config.get(config_name)
    if not check_config:
        raise ValueError(f'config whith name {config_name} does not exist.')

    app = Flask(__name__)
    app.config.from_object(check_config)

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(main, url_prefix='')
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(blogs, url_prefix='/blogs')

    filters.FILTERS['is_list'] = is_list

    return app


from model import Buttons, Location
