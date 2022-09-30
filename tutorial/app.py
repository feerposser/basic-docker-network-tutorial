from flask import Flask, jsonify
from flask_mongoengine import MongoEngine


app = Flask(__name__)

#mongoengine config
app.config["MONGODB_SETTINGS"] = {
    "db": "example", # database name
    "host": "mongo", # host (container) name
    "username": "admin",
    "password": "admin",
    'authentication_source': 'admin'
}

db = MongoEngine()

# default document
class Model(db.Document):
    name = db.StringField(required=True)
    
    def __str__(self):
        return self.name

db.init_app(app)

@app.route("/")
def index():
    # get all the data and cast into a JSON
    return jsonify(Model.objects.all())

@app.route("/test")
def test():
    return "It works!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
