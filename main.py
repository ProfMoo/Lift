import argparse

def enter_workout():
	workout = input("What workout did you do?")

def loop():
	while (1):
		command = input("Enter command\n")

		if command == "help" or command == "Help" or command == "HELP":
			print("todo: help")

		if command == "Enter Workout":
			enter_workout()

if __name__ == "__main__":
	print("Welcome to Dr. Moo's programming helper")
	print("Type \"help\" for help")
	loop()