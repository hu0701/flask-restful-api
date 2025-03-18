from routes import app
from flask import jsonify, request


@app.route('/students/<stedent_id>')
def get_student(stedent_id):
    if request.is_json:
        args = request.get_json()
    student = {'id': stedent_id, 'name': 'John Doe', 'gender': 'Male'}

    return jsonify(student)