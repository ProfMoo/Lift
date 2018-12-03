class LiftSession(object):
	def __init__(self, lift_name):
		self.sets = []
		self.lift_name = lift_name

	def add_set(self, reps, rpe):
		self.sets.append((reps, rpe))

	def __str__(self):
		to_return = ""
		to_return += "Lift: " + self.lift_name + " | "
		for s in self.sets:
			to_return += "(" + str(s[0]) + "@" + str(s[1]) + ")"
		return to_return