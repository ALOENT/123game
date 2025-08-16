from modes.easybot import easy_bot
from modes.regular import regular_game
from modes.extreme import extreme_bot


def main():
	
	# Greetings 
	print("Welcome to the game of Stone, Paper, Scissor!")
	print("GAME MODES:")
	print("1. EasyBot(Scoring probability is 75%)")
	print("2. Regular Game")
	print("3. Extreme Difficulty(Scoring probability is 10%)")
	print("NOTE: Every mode except 'Regular Game' allows you to use admin commands.")

	while True:
		try:
			ch = int(input("Enter game mode(1, 2 or 3): "))
			if ch not in [1, 2, 3]:
				print("Invalid choice! Please choose a valid game mode.")
				continue
		except ValueError:
			print("Invalid input! Please enter a number (1, 2 or 3).")
			continue
		break

	if ch==1:
		easy_bot()
	elif ch==2:
		regular_game()
	elif ch==3:
		extreme_bot()


if __name__ == "__main__":

	main()