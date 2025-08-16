from utils import options, WIN_SCORE, commands, print_rules, cheats_check


def easy_bot():
	"""
	Function to play the easy bot game with a 75% probability of scoring.
	"""
	print("------------------------------------------------------------------------")
	print("Starting EasyBot mode...")
	print_rules()

	# User and Computer Scores
	comp_score = 0
	user_score = 0

	# Main game loop
	while comp_score<WIN_SCORE and user_score<WIN_SCORE:
		try:
			user = input(f"Enter your choice: ")
			# If choice is not valid 
			if user not in list(options.keys()) and user not in commands:
				print(f"Invalid choice!!!\nChoose from these options: {options}")
				continue
		except ValueError:
			print("Invalid input! Please enter a number (1, 2 or 3).")
			continue
		
		user, comp = cheats_check(user, "easy")

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
		print("Computer WON !!!\nEasyBot se haar gya chomu XD!!!")
	else :
		print("tu jit gya ladlee !!!") 

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print("Game Over!")