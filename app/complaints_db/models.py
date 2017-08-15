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

	# def __repr__(self):
	# 	return "{first_name",self.first_name,"}"
	# def get_all(db.model):
		# users = this
