import random
import colorama
from colorama import Fore, Back, Style
from utils import options, WIN_SCORE, print_rules, update_scores, check_winner
colorama.init(autoreset=True)


def regular_game():
	"""
	Function to play the regular game without admin commands and randomness.
	"""

	print("-----------------------------------------------------------------------")
	print(f"{Fore.YELLOW}{Back.BLACK}Starting Regular game...")
	print_rules()

	# User and Computer Scores
	comp_score = 0
	user_score = 0

	# Main game loop
	while comp_score<WIN_SCORE and user_score<WIN_SCORE:
		
		try:
			user = input(f"Enter your choice: ")
			if user not in list(options.keys()):
				print(f"{Fore.LIGHTMAGENTA_EX}Invalid choice!!!\nChoose from these options: {options}")
				continue
		except ValueError:
			print("Invalid input! Please enter a number (1, 2 or 3).")
			continue

		comp = random.choice(list(options.keys()))

		print(f"{Back.BLACK}Computer's choice: {options[comp]}\tYour choice: {options[user]}")

		user_score, comp_score = update_scores(user, comp, user_score, comp_score)

		print(f"Computer's score: {comp_score} \t User's score: {user_score}")
		print("-----------------------------------------------------------------------")

	# Check for game end
	check_winner(comp_score, user_score, game_mode="regular")

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print(f"{Fore.WHITE}{Back.YELLOW}Game Over!")
