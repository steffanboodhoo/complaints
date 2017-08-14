from app import App
from flask import request
from pprint import pprint

@App.route('/')
@App.route('/home', methods=['GET'])
def main():
	return App.send_static_file('main/home.html')


