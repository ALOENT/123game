import colorama
from colorama import Fore, Back, Style
from utils import options, commands, WIN_SCORE, cheats_check, print_rules, update_scores, check_winner
colorama.init(autoreset=True)


def extreme_bot():
	"""
	Function to play the extreme bot game with a 10% probability of scoring.
	"""
	print("------------------------------------------------------------------------")
	print(f"{Fore.YELLOW}{Back.BLACK}Starting ExtremeBot mode...")
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
				print(f"{Fore.LIGHTMAGENTA_EX}Invalid choice!!!\nChoose from these options: {options}")
				continue
		except ValueError:
			print("Invalid input! Please enter a number (1, 2 or 3).")
			continue
		
		user, comp = cheats_check(user, "hard")

		print(f"Computer's choice: {options[comp]}\tYour choice: {options[user]}")
		
		user_score, comp_score = update_scores(user, comp, user_score, comp_score)

		print(f"{Back.BLACK}Computer's score: {comp_score} \t User's score: {user_score}")
		print("-----------------------------------------------------------------------")

	# Check for game end
	check_winner(comp_score, user_score, game_mode="hard")

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print(f"{Fore.WHITE}{Back.YELLOW}{Style.BRIGHT}Game Over!")