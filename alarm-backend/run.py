from sqlalchemy import true
from alarm import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4444", debug=True)

