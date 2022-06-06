"""
Server content
and initials values.
"""

from flask import Flask
from routes.monitor import monitor


# creating the server
app = Flask(__name__)


# using routes
app.register_blueprint(monitor)
