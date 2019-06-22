from flask import Flask
from config import Config


def create_app(config=Config):
    app = Flask(__name__)

    return app
