class Lift(object):
	def __init__(self, reps, weight, rpe):
		self.reps = reps
		self.weight = weight
		self.rpe = rpe

	def __str__(self):
		return self.reps + "w/" + self.weight + "@" + self.rpe