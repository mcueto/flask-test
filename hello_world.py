"""Flask hello_world project"""
import os
from flask import (
    Flask,
    render_template,
)
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/greetings")
def greetings():
    greeting_list = mongo.db.greetings.find({})

    return render_template(
        "greetings.html",
        greeting_list=greeting_list
    )
