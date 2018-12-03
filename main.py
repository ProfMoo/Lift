import argparse
from session import *
from liftsession import *

sessions = []

def view_sessions():
	i = 0
	while (i < len(sessions)):
		print(sessions[i])
		i += 1

def enter_workout():
	try:
		workout = input("How many movements did you do? ")
		workout = int(workout)
	except:
		print("You need to enter a number ")
		return
	session = Session()
	i = 0
	while (i < workout):
		lift = input("What lift did you perform? ")
		lift_session = LiftSession(lift)
		sets = input("How many sets did you perform? ")
		sets = int(sets)
		j = 0
		while (j < sets):
			reps = input("Reps? ")
			rpe = input("Rpe? ")
			lift_session.add_set(reps, rpe)
			j += 1
		session.add_session_lift(lift_session)
		i += 1
	print("Completed entering a workout. Here is your info:")
	print(session)
	sessions.append(session)

def loop():
	while (1):
		command = input("Enter command\n")

		if command == "help" or command == "Help" or command == "HELP":
			print("todo: help")

		if command == "Enter Workout":
			enter_workout()

		if command == "View" or command == "view":
			view_sessions()

if __name__ == "__main__":
	print("Welcome to Dr. Moo's programming helper ")
	print("Type \"help\" for help")
	loop()