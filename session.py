class Session(object):
	def __init__(self):
		self.date = "12-02-2018"
		self.session_lifts = []

	def add_session_lift(self, session_lift):
		self.session_lifts.append(session_lift)

	def __str__(self):
		to_return = ""
		to_return += "Date: " + self.date
		to_return += "\n===================\n"
		i = 0
		while (i < len(self.session_lifts)):
			to_return += str(self.session_lifts[i]) + "\n"
			i += 1
		return to_return