from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__, static_url_path="/", static_folder="../static")
app.config['SECRET_KEY'] = "changeMe"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../alarm.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


from alarm import routes
from alarm import models