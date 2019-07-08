from application import create_app
from database import db
from model import Buttons, Location

app = create_app('development')


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Buttons': Buttons, 'Location': Location}
