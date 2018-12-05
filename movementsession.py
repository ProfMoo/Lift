class MovementSession(object):
	def __init__(self, lift_name):
		self.sets = []
		self.lift_name = lift_name

	def add_lift(self, lift):
		self.sets.append(lift)

	def __str__(self):
		to_return = ""
		to_return += "Lift: " + self.lift_name + " |"
		for s in self.sets:
			to_return += " " + str(s)
		return to_return