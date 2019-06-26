from flask_restful import (
    Resource,
)


class GreetingsResource(Resource):
    def get(self):
        return [
            {
                "message": "hello world"
            }
        ]
