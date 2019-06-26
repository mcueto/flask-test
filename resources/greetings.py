from flask_restful import (
    reqparse,
    abort,
    Resource,
)


class GreetingResource(Resource):
    def get(self, greeting_id):
        return {
            "message": "hello world"
        }


class GreetingListResource(Resource):
    def get(self):
        return [
            {
                "message": "hello world"
            }
        ]
