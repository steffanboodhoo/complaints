from app import App
from flask import request, session
from pprint import pprint

import json

#remove after
from complaints_db import db

@App.route('/')
@App.route('/home', methods=['GET'])
def main():
	return App.send_static_file('home/home.html')


@App.route('/authenticate', methods=['POST'])
def authenticate():
	data = request.get_json()
	pprint(data)
	pprint(data['id'])
	return 'pew pew'

@App.route('/users',methods=['GET','POST'])
def users():
	results = None
	if request.method == 'GET':
		results = db.getEmployee()
		pprint(results)
		results = json.dumps(results)
	elif request.method == 'POST':
		results = 'NOTHING YET'

	return results

@App.route('/issues',methods=['GET','POST'])
def issues():
	results = {"status":"failure"}
	if request.method == 'GET':
		results['data'] = db.getIssue()
		results['status'] = 'success'
		results = json.dumps(results)
	elif request.method == 'POST':
		results = 'NOTHING YET'

	return results


@App.route('/teams',methods=['GET','POST'])
def teams():
	results = None
	if request.method == 'GET':
		results = db.getTeam()
		pprint(results)
		results = json.dumps(results)
	elif request.method == 'POST':
		results = 'NOTHING YET'

	return results
