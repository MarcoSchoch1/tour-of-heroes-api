from types import MethodDescriptorType
import flask, string
from flask import jsonify, request
from flask import json
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

all_heroes = [ { 'id': 11, 'name': 'Dr Nice' },
  { 'id': 12, 'name': 'Narco' },
  { 'id': 13, 'name': 'Bombasto' },
  { 'id': 14, 'name': 'Celeritas' },
  { 'id': 15, 'name': 'Magneta' },
  { 'id': 16, 'name': 'RubberMan' },
  { 'id': 17, 'name': 'Dynama' },
  { 'id': 18, 'name': 'Dr IQ' },
  { 'id': 19, 'name': 'Magma' },
  { 'id': 20, 'name': 'Tornado' }]

@app.route('/heroes', methods=['GET'])
def heroes():
    return jsonify(all_heroes)

@app.route('/detail/<id>', methods=['GET'])
def detail(id):
    for hero in all_heroes:
        if int(hero['id']) == int(id):
            return jsonify(hero)
    return "{'No hero found!'}", 400

@app.route('/update', methods=['POST'])
def update():
    data = request.data
    decodedData = data.decode('UTF-8')
    data = eval(decodedData)
    for hero in all_heroes:
        if hero['id'] == data['id']:
            hero['name'] = data['name']
            return hero
    return "Hero not found", 400

app.run()