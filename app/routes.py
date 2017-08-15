from app import App
from flask import request, session
from pprint import pprint
import json
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
