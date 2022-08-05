from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hi, there!"

@app.route("/<name>")
def nome(name):
    return "Hi, {}!".format(name)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
