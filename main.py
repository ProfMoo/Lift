import argparse
from session import *
from movementsession import *
from lift import *

sessions = []

def view_sessions():
	i = 0
	while (i < len(sessions)):
		print(sessions[i])
		i += 1

def tab_prompt(num_tabs, input_str):
	to_return = (" " * num_tabs) + input_str + " "
	return str(to_return)

def enter_workout():

	workout = input(tab_prompt(1, "How many movements did you do?"))
	workout = int(workout)

	session = Session()
	i = 0
	while (i < workout):
		lift = input(tab_prompt(2, "What lift did you perform?"))
		movement_session = MovementSession(lift)
		sets = input(tab_prompt(2, "How many sets did you perform?"))
		sets = int(sets)
		j = 0
		while (j < sets):
			reps = input(tab_prompt(3, "Reps?"))
			weight = input(tab_prompt(3, "Weight?"))
			rpe = input(tab_prompt(3, "Rpe?"))
			movement_session.add_lift(Lift(reps, weight, rpe))
			j += 1
		session.add_movement_session(movement_session)
		i += 1
	print("Completed entering a workout. Here is your info:")
	print(session)
	sessions.append(session)

def loop():
	while (1):
		command = input("Enter Command: ")

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