"""Flask hello_world project"""
import os
from flask import (
    Flask,
    render_template,
)
from flask_restful import (
    # Resource,
    Api,
)
from flask_pymongo import PyMongo
from resources.greetings import (
    GreetingResource,
    GreetingListResource,
)

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Initialize the REST API instance
api = Api(app)
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


# Register the GreetingsResource resource on the REST API
api.add_resource(
    GreetingListResource,
    '/api/greetings'
)
api.add_resource(
    GreetingResource,
    '/api/greetings/<greeting_id>'
)


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )
