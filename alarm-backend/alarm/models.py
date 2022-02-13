from alarm import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    craig_alarms = db.relationship('CraiglistAlarm', backref="user", lazy=True)

    def __repr__(self) -> str:
        return f"User({self.username})"

class CraiglistAlarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    data = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self) -> str:
        return f"Craiglist Alarm (${self.url})"
    

db.create_all()