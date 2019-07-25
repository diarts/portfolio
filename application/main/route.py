from flask import render_template, redirect, url_for
from . import main
from model import Buttons, Location
from flask_login import current_user
from application.help_func.work_with_buttons import add_button_child
from sqlalchemy import or_


@main.route('/', methods=['GET'])
def index_redirect():
    return redirect(url_for('main.index'))


@main.route('/main/', methods=['GET'])
def index():
    buttons_dict = {}

    nav_buttons_list = []
    nav_buttons = Buttons.query.filter(Buttons.location.any(location='nav'), Buttons.parent_id == None,
                                       or_(Buttons.is_loggin == None, Buttons.is_loggin == True)).order_by(
        Buttons.parent_id, Buttons.sort_index).all()

    for button in nav_buttons:
        if button.child_buttons:
            button_with_child = [button, ]
            button_with_child.append(add_button_child(button.child_buttons))
            nav_buttons_list.append(button_with_child)
        else:
            nav_buttons_list.append(button)

    buttons_dict['nav'] = nav_buttons_list

    return render_template('main_page.html', buttons_dict=buttons_dict)
