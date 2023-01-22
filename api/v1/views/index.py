#!/usr/bin/python3
"""
    The landing page of the web app
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON"""

    return jsonify({"status": "OK"})


@app_views.route('/api/vi/stats', methods=['GET'])
def stats():
    """Displays a JSON"""

    objects = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(objects)
