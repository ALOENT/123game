from utils import options, commands, WIN_SCORE, cheats_check, print_rules
	

def extreme_bot():
	"""
	Function to play the extreme bot game with a 10% probability of scoring.
	"""
	print("------------------------------------------------------------------------")
	print("Starting ExtremeBot mode...")
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
		
		user, comp = cheats_check(user, "hard")

		print(f"Computer's choice: {options[comp]}\tYour choice: {options[user]}")
		if user == comp:
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
		print("Computer WON !!!\nKaidee me rahiyee Chhotee, Wrna g*nd pe lagenge sotteee!!!")
	else :
		print("tu jit gya ladlee\nLuck bhari h aaj tera!!!") 

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print("Game Over!")