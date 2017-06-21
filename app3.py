#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import user

app = Flask(__name__)

tasks = [
    {

    }
]

@auth.get_password
def get_password(username):
    if username == 'ken':
	return 'Passw0rd!'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/createuser', methods=['POST'])
@auth.login_required
def createuser():
	function = {
		'username' : request.json['username'],
		'passwd' : request.json['passwd'],
		'fname' : request.json['fname']
	}
	tasks.append(function)
	user.createuser(function['username'],function['passwd'],function['fname'])
	return jsonify({'users' : user.readuser()})
@app.route('/readuser', methods=['GET'])
def readuser():
	return jsonify({'users' : user.readuser()})

@app.route('/deluser', methods=['POST'])
@auth.login_required
def deluser():
	function = {
		'username' : request.json['username']
	}
	tasks.append(function)
	user.deluser(function['username'])
	return jsonify({'users' : user.readuser()})
@app.route('/updateuser', methods=['POST'])
@auth.login_required
def updateuser():
	function = {
		'username' : request.json['username'],
		'username1' : request.json['username1'],
                'passwd' : request.json['passwd'],
                'fname' : request.json['fname']
        }
	tasks.append(function)
	user.updateuser(function['username'],function['username1'],function['passwd'],function['fname'])
	return jsonify({'users' : user.readuser()})

@app.route('/createssh', methods=['POST'])
@auth.login_required
def createssh():
	#function = {
	#	'usr' : request.json['usr']
	#}
	#tasks.append(function)
	#user.createssh(function['usr'])
	usr = request.json['usr']
	user.createssh(usr)
	return jsonify({'ssh' : "created"})

@app.route('/readssh', methods=['POST'])
@auth.login_required
def readssh():
	function = {
		'usr' : request.json['usr']
	}
	tasks.append(function)
	#user.readssh(function['usr'])
	return jsonify({'ssh' : user.readssh(function['usr'])})

@app.route('/delssh', methods=['POST'])
@auth.login_required
def delssh():
	usr = request.json['usr']
	user.delssh(usr)
	return jsonify({'ssh' : "deleted"})

@app.route('/updatessh', methods=['POST'])
@auth.login_required
def updatessh():
	usr = request.json['usr']
	user.updatessh(usr)
	return jsonify({'ssh' : "updated"})

if __name__ == '__main__':
    app.run(debug=True)

