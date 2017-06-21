#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import nameserver

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

@app.route('/createnameserver', methods=['POST'])
@auth.login_required
def createnameserver():
        function = {
                'ip' : request.json['ip']
        }
        tasks.append(function)
        nameserver.createnameserver(function['ip'])
        return jsonify({'nameserver' : nameserver.readnameserver()})

@app.route('/readnameserver', methods=['GET'])
def readnameserver():
        return jsonify({'nameserver' : nameserver.readnameserver()})

@app.route('/delnameserver', methods=['POST'])
@auth.login_required
def delnameserver():
        function = {
                'ip' : request.json['ip']
        }
        tasks.append(function)
        nameserver.delnameserver(function['ip'])
        return jsonify({'nameserver' : nameserver.readnameserver()})

@app.route('/updatenameserver', methods=['POST'])
@auth.login_required
def updatenameserver():
        function = {
                'ip' : request.json['ip'],
                'ip1' : request.json['ip1']
        }
        tasks.append(function)
        nameserver.updatenameserver(function['ip'],function['ip1'])
        return jsonify({'nameserver' : nameserver.readnameserver()})

if __name__ == '__main__':
    app.run(debug=True)

