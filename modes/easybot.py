import colorama
from colorama import Fore, Back, Style
from utils import options, WIN_SCORE, commands, print_rules, cheats_check, update_scores, check_winner
colorama.init(autoreset=True)


def easy_bot():
	"""
	Function to play the easy bot game with a 75% probability of scoring.
	"""
	print("------------------------------------------------------------------------")
	print(f"{Fore.YELLOW}{Back.BLACK}Starting EasyBot mode...")
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
		
		user, comp = cheats_check(user, "easy")

		print(f"{Back.BLACK}Computer's choice: {options[comp]}\tYour choice: {options[user]}")

		user_score, comp_score = update_scores(user, comp, user_score, comp_score)

		print(f"Computer's score: {comp_score} \t User's score: {user_score}")
		print("-----------------------------------------------------------------------")

	# Check for game end
	check_winner(comp_score, user_score, game_mode="easy")

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print(f"{Fore.WHITE}{Back.YELLOW}Game Over!")