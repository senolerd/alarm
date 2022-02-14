from flask import request
from alarm import app, db
from alarm.blueprints.craiglist import craiglistBP
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from alarm.models import User, CraiglistAlarm

app.register_blueprint(blueprint=craiglistBP)


@app.route('/')
def index():
    return {"status": "ok"}


@app.route("/login", methods=["POST"])
def login():

    form_data = request.get_json()
    email, password = form_data['email'], form_data['password']

    if email and password:
        # If username and password are exist

        try:
            user = User.query.filter_by(email=email).first()
            check_password_hash(user.password, password)
            token = jwt.encode({"email":user.email},app.secret_key, algorithm="HS256")
            return {"token": token}, 200

        except:
            return {"error":"Authentication error."}, 401   

    else:
            return {"error":"Credential required."}, 401   


@app.route("/register", methods=["POST"])
def register():
    form_data = request.get_json()
    email, password = form_data['email'], form_data['password']

    if email and password:
        # email and password are exist

        user = User.query.filter_by(email=email).first()
        if not user:
            newUser = User(email=email, password=generate_password_hash(password))
            try:
                db.session.add(newUser)
                db.session.commit()
                return {"status":"User is registered"},200
            except Exception as e:
                return {"error":"[e112] Someting went wrong while creating account."},400
        else:
            return {"status":"User exist"},400
    else:
        return {"status":"Username and/or password is required."},400



