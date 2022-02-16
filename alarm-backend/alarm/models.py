from email.policy import default
from alarm import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    craig_alarms = db.relationship('CraiglistAlarm', backref="user", lazy=True)

    def __repr__(self) -> str:
        return f"User(username: {self.username}, email: {self.email})"

    def get_id(self):
        return self.email
    

class CraiglistAlarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="Unnamed")
    url = db.Column(db.String)
    data = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self) -> str:
        return f"Craiglist Alarm (${self.url})"
    

db.create_all()