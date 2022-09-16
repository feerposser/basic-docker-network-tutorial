from flask import Flask, jsonify
from flask_mongoengine import MongoEngine


app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    "db": "example",
    "host": "mongo",
    "username": "admin",
    "password": "admin",
    'authentication_source': 'admin'
}

db = MongoEngine()

class Model(db.Document):
    name = db.StringField(required=True)
    
    def __str__(self):
        return self.name

db.init_app(app)

@app.route("/")
def index():
    return jsonify(Model.objects.all())

if __name__ == "__main__":
    app.run(host="0.0.0.0")
