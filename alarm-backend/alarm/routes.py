from alarm import app
from alarm.blueprints.craiglist import craiglistBP


@app.route('/')
def index():
    return {"status":"ok"}


app.register_blueprint(blueprint=craiglistBP)