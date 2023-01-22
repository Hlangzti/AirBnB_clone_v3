#!/usr/bin/python3
"""
    Flask API for AirBnB_clone
"""

import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_storage():
    """calls storage.close()"""

    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """not found error handler"""

    return jsonify({'error': 'Not found'})


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST") or "0.0.0.0"
    port = os.environ.get("HBNB_API_PORT") or 5000
    app.run(host=host, port=port, threaded=True)
