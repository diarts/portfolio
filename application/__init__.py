from flask import Flask
from config import config
from database import db
from application.main import main
from application.users import users
from application.blogs import blogs


def create_app(config_name=config.get('default')):
    if not config_name:
        raise ValueError('default configuration for flask application does not exist.')
    check_config = config.get(config_name)
    if not check_config:
        raise ValueError(f'config whith name {config_name} does not exist.')

    app = Flask(__name__)
    app.config.from_object(check_config)

    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(blogs, url_prefix='/blogs')

    return app
