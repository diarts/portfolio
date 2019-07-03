from flask import render_template, redirect, url_for
from . import main
from datetime import datetime


@main.route('/', methods=['GET'])
def index_redirect():
    return redirect(url_for('main.index'))

@main.route('/main/', methods=['GET'])
def index():
    return render_template('base.html', time=datetime.utcnow())