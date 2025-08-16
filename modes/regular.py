import random
import utils as utils
from utils import options, WIN_SCORE


def regular_game():
	"""
	Function to play the regular game without admin commands and randomness.
	"""

	print("-----------------------------------------------------------------------")
	print("Starting regular game...")
	utils.print_rules()

	# User and Computer Scores
	comp_score = 0
	user_score = 0

	# Main game loop
	while comp_score<WIN_SCORE and user_score<WIN_SCORE:
		
		try:
			user = input(f"Enter your choice: ")
			if user not in list(options.keys()):
				print(f"Invalid choice!!!\nChoose from these options: {options}")
				continue
		except ValueError:
			print("Invalid input! Please enter a number (1, 2 or 3).")
			continue

		comp=random.choice(list(options.keys()))

		print(f"Computer's choice: {options[comp]}\tYour choice: {options[user]}")
		if user==comp:
			print("Its a tie! ")
		elif (user=="1" and comp== "3") or (user=="2" and comp=="1") or (user=="3" and comp=="2"):
			print("You Scored !!!!")
			user_score += 1

		elif (user=="3" and comp=="1") or (user=="2" and comp=="3") or (user=="1" and comp=="2"):
			print("Computer Scored !!!!!")
			comp_score+=1

		print(f"Computer's score: {comp_score} \t User's score: {user_score}")
		print("-----------------------------------------------------------------------")

	# Check for game end
	if comp_score==WIN_SCORE : 
		print("Computer WON !!! ")
	else :
		print("tu jit gya ladlee !!!") 

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print("Game Over!")
