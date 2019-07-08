from database import db
from sqlalchemy.dialects.mysql import SMALLINT, VARCHAR, BOOLEAN

locations = db.Table('button-location',
                     db.Column('button_id', SMALLINT, db.ForeignKey('buttons.id'), primary_key=True),
                     db.Column('location_id', SMALLINT, db.ForeignKey('location.id'), primary_key=True)
                     )


class Buttons(db.Model):
    """table stored web application buttons
    :param link - link to route function like (blueprint.route_function_name)
    """
    __tablename__ = 'buttons'

    id = db.Column(SMALLINT, primary_key=True)
    ru_text = db.Column(VARCHAR(20), nullable=False, default='__EMPTY__')
    eng_text = db.Column(VARCHAR(20), nullable=False, default='__EMPTY__')
    link = db.Column(VARCHAR(30), nullable=False, default='__EMPTY__')
    is_loggin = db.Column(BOOLEAN, nullable=True)
    sort_index = db.Column(SMALLINT, nullable=False, default=-1)
    parent_id = db.Column(SMALLINT, db.ForeignKey('buttons.id'), nullable=True)

    location = db.relationship('Location', secondary=locations, lazy='dynamic',
                               backref=db.backref('buttons', lazy='dynamic'))
    child_buttons = db.relationship('Buttons', backref=db.backref('parent', remote_side=id))

    def __repr__(self):
        a = f'<class Buttons id = {self.id} ru_text = {self.ru_text} eng_text = {self.eng_text} link = {self.link} ' \
            f'is_loggin = {self.is_loggin} sort_index = {self.sort_index} parrent_id = {self.parent_id}>'
        return a


class Location(db.Model):
    """table with button location type"""
    __tablename__ = 'location'

    id = db.Column(SMALLINT, primary_key=True)
    location = db.Column(VARCHAR(20), nullable=False, default='__EMPTY__')

    def __repr__(self):
        return f'<class "Button location" id = {self.id} location = {self.location}>'