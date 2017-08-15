from models import employee, issue, Team
from app import db
from pprint import pprint 

def addEmployee(first_name, last_name, user_id, team_id):
	new_employee = employee(first_name, last_name, user_id, team_id)
	db.session.add(employee)
	db.session.commit()

# def addIssue():


def getEmployee():
	# data = None
	# if query_obj is None:
	data = employee.query.all()

	results = []
	for row in data:
		#remove unwanted field
		del row.__dict__['_sa_instance_state']
		#convert to dictionary and append to results
		results.append(row.__dict__)
	return results


def getIssue():
	data = issue.query.all()

	results = []
	for row in data:
		#remove unwanted field
		del row.__dict__['_sa_instance_state']
		#convert to dictionary and append to results
		results.append(row.__dict__)
	return results


def getTeam():
	data = Team.query.all()

	results = []
	for row in data:
		#remove unwanted field
		del row.__dict__['_sa_instance_state']
		#convert to dictionary and append to results
		results.append(row.__dict__)
	return results
