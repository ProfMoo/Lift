class Session(object):
	def __init__(self):
		self.date = "12-02-2018"
		self.movement_sessions = []

	def add_movement_session(self, movement_session):
		self.movement_sessions.append(movement_session)

	def __str__(self):
		to_return = ""
		to_return += "Date: " + self.date
		to_return += "\n===================\n"
		for movement_session in self.movement_sessions:
			to_return += str(movement_session) + "\n"
		return to_return