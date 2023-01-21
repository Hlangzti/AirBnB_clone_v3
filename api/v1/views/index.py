#!/usr/bin/python3
"""
    The landing page of the web app
"""

from api.v1.views import app_views
import json

@app_views.route('/status', methods=['GET'])
def status():
    """Returns a JSON"""

    return json.dumps({"status":"OK"})
