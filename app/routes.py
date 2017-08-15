from app import App
from flask import request, session
from pprint import pprint
import json

#remove after
from complaints_db import db

@App.route('/')
@App.route('/home', methods=['GET'])
def main():
	return App.send_static_file('main/home.html')


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
		results = db.getEmployeeAll()
		pprint(results)
		results = json.dumps(results)
	elif request.method == 'POST':
		results = 'NOTHING YET'

	return results
