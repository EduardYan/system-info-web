#!/usr/bin/env python3

"""
Principal file to start
the server.
"""

from app import app
from helpers.config import OBJECT

if __name__ == '__main__':
    app.run(
        port = OBJECT['PORT'],
        debug = OBJECT['DEBUG'],
        host = '0.0.0.0',
    )
