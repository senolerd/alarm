from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = "changeMe"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///alarm.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)


from alarm import routes

