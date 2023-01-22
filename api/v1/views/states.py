#!/usr/bin/python3
"""
    View for State objects
"""

from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.state import State

app_views.url_map.strict_slashes = False


@app_views.route('/api/v1/states', methods=['GET'])
def list_states():
    """Lists all State objects"""

    all_states = storage.all('State').values()
    states = list()
    for obj in all_states:
        states.append(obj.to_dict())

    return jsonify(states)


@app_views.route('/api/v1/states/<state_id>', methods=['GET'])
def get_state_obj(state_id):
    """Retrieves a state object"""

    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    state = state.to_dict()

    return jsonify(state)


@app_views.route('/api/v1/states/<state_id>', methods=['DELETE'])
def delete_state_obj(state_id):
    """Deletes a state object"""

    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/api/v1/states', methods=['POST'])
def post_state():
    """Post a state"""

    data = request.json
    if not data:
        abort(400, "Not a JSON")

    if 'name' not in data.keys():
        abort(400, "Missing name")
    instance = State(**data)
    storage.new(instance)
    storage.save()

    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/api/v1/states/<state_id>', methods=['POST'])
def update_state(state_id):
    """Updates a state object"""

    state = storage.get('State', state_id)
    if state is None:
        abort(404)
    data = request.json
    if not data:
        abort(400, "Not a JSON")

    for key, value in data.items():
        setattr(state, key, value)

    storage.save()

    return make_response(jsonify(state.to_dict()), 200)
