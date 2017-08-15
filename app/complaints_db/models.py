from app import db

class employee(db.Model):
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
	user_id = db.Column(db.Integer, primary_key=True)
	team_id = db.Column(db.Integer)

	def __init__(self, first_name, last_name, user_id, team_id):
		self.first_name = first_name
		self.last_name = last_name
		self.user_id = user_id
		self.team_id = team_id

class issue(db.Model):
	issue_id = db.Column(db.Integer, primary_key=True)
	status = db.Column(db.String(15))
	date_created = db.Column(db.Date)
	creator_id = db.Column(db.Integer)
	date_resolved = db.Column(db.Date)
	resolver_id = db.Column(db.Integer)
	issue_team_id = db.Column(db.Integer)
	description = db.Column(db.String)

	def __init__(self, issue_id, status, date_created, creator_id, date_resolved, resolver_id, issue_team_id, description):
		self.issue_id = issue_id
		self.status = status
		self.date_created = date_created
		self.creator_id = creator_id
		self.date_resolved = date_resolved
		self.resolver_id = resolver_id
		self.issue_team_id = issue_team_id
		self.description = description

class Team(db.Model):
	# __tablename__ = 'Team'
	Name = db.Column(db.String(20))
	team_id = db.Column(db.Integer, primary_key=True)

	def __init__(self, Name, team_id):
		self.Name = Name
		self.team_id = team_id

	# def __repr__(self):
	# 	return "{first_name",self.first_name,"}"
	# def get_all(db.model):
		# users = this
