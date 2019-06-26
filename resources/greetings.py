"""greetings resources module."""
from flask_restful import (
    reqparse,
    abort,
    Resource,
)

parser = reqparse.RequestParser()
parser.add_argument('message')

GREETINGS = {
    '1': {
        "message": "hello world"
    },
    '2': {
        "message": "hola mundo"
    },
    '3': {
        "message": "hola mundito"
    }
}


class GreetingResource(Resource):
    def get(self, greeting_id):
        """Retrieve an specific Greeting based on it's id."""
        return GREETINGS[greeting_id]

    def delete(self, greeting_id):
        """Remove an specific Greeting based on it's id."""
        # abort_if_todo_doesnt_exist(todo_id)
        del GREETINGS[greeting_id]
        return '', 204

    def put(self, greeting_id):
        """Update an specific Greeting based on it's id."""
        args = parser.parse_args()
        message = {'message': args['message']}
        GREETINGS[greeting_id] = message

        return message, 201


class GreetingListResource(Resource):
    def get(self):
        return GREETINGS

    def post(self):
        args = parser.parse_args()
        # We're "adding" a new Greeting so it's id will be 'max plus one'
        greeting_id = int(
            max(
                GREETINGS.keys()
            ).lstrip('todo')
        ) + 1

        greeting_id = 'greeting%i' % greeting_id
        GREETINGS[greeting_id] = {'greeting': args['message']}

        return GREETINGS[greeting_id], 201
