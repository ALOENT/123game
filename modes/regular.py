import random
import utils as utils


def regularGame():
	"""
	Function to play the regular game without admin commands and randomness.
	"""

	print("-----------------------------------------------------------------------")
	print("Starting regular game...")
	print("RULES:\n1.You can enter your choice as a number (1 for stone, 2 for paper, 3 for scissor).\n2. First to score 11 points wins the game.")

	options = {1: "stone", 2: "paper", 3: "scissor"}
	# User and Computer Scores
	compS=0
	userS=0

	# Main game loop
	while compS<11 and userS<11:
		
		try:
			user = int(input(f"Enter your choice: "))
			if user not in [1, 2, 3]:
				print(f"Invalid choice!!!\nChoose from these options: {options}")
				continue
		except ValueError:
			print("Invalid input! Please enter a number (1, 2 or 3).")
			continue

		comp=random.choice(list(options.keys()))
		print(f"Computer's choice: {options[comp]}\tYour choice: {options[user]}")
		if user==comp:
			print("Its a tie! ")
		elif (user==1 and comp== 3) or (user==2 and comp==1) or (user==3 and comp==2):
			print("You Scored !!!!")
			userS += 1

		elif (user==3 and comp==1) or (user==2 and comp==3) or (user==1 and comp==2):
			print("Computer Scored !!!!!")
			compS+=1
		print(f"Computer's score: {compS} \t User's score: {userS}")
		print("-----------------------------------------------------------------------")

	# Check for game end
	if compS==11 : 
		print("Computer WON !!! ")
	else :
		print("tu jit gya ladlee !!!") 

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print("Game Over!")
