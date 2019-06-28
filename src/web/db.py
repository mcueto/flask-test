"""flask-test database module."""
from flask import (
    current_app,
    g,
)
from flask_pymongo import PyMongo


def get_mongo():
    if 'mongo' not in g:
        # Initialize mongodb for current app
        g.mongo = PyMongo(current_app)

    return g.mongo
