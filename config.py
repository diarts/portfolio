import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))


class Config():
    FLASK_ENV = 'production'
    SECRET_KEY_LENGTH = int(os.environ.get('SECRET_KEY_LENGTH'))
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(SECRET_KEY_LENGTH)

    JSON_SORT_KEYS = bool(os.environ.get('JSON_SORT_KEYS'))

    SQLALCHEMY_COMMIT_ON_TEARDOWN = bool(os.environ.get('SQLALCHEMY_COMMIT_ON_TEARDOWN'))
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')


class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


class Develop(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:user@localhost/portfolio_develop'


class Testing(Develop):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'mysql://user:user@localhost/portfolio_test'


config = {
    'development': Develop,
    'testing': Testing,
    'production': Production,

    'default': Develop,
}
