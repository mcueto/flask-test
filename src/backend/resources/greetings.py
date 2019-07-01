"""greetings resources module."""
import json
import uuid
from flask_restful import (
    reqparse,
    Resource,
)
from db import (
    get_mongo,
)
from bson.json_util import (
    dumps as bson_dumps,
    loads as bson_loads,
)


parser = reqparse.RequestParser()
parser.add_argument('message')


class GreetingResource(Resource):
    def get(self, greeting_id):
        """Retrieve an specific Greeting based on it's id."""
        greeting = get_mongo().db.greetings.find(
            {
                'unique_id': greeting_id
            }
        )

        return json.loads(
            bson_dumps(greeting)
        )

    def delete(self, greeting_id):
        """Remove an specific Greeting based on it's id."""
        greeting = get_mongo().db.greetings.delete_one(
            {
                'unique_id': greeting_id
            }
        )

        return '', 204

    def put(self, greeting_id):
        """Update an specific Greeting based on it's id."""
        args = parser.parse_args()
        message = {'message': args['message']}

        greeting_filter = {
            'unique_id': greeting_id
        }
        greeting_data = {
            'message': message
        }

        greeting = get_mongo().db.greetings.find_one_and_update(
            greeting_filter,
            {
                '$set': greeting_data
            }
        )

        return message, 201


class GreetingListResource(Resource):
    def get(self):
        greeting_list = get_mongo().db.greetings.find({})

        return json.loads(
            bson_dumps(greeting_list)
        )

    def post(self):
        args = parser.parse_args()
        # We're "adding" a new Greeting so it's id will be 'max plus one'
        # greeting_id = get_mongo().db.greetings.count_documents({})
        greeting_id = str(uuid.uuid4())
        message = args['message']

        greeting_data = {
            'unique_id': greeting_id,
            'message': message
        }

        result = get_mongo().db.greetings.insert_one(
            greeting_data
        )

        greeting_data = json.loads(
            bson_dumps(greeting_data)
        )

        return greeting_data, 201
