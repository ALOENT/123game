from modes.easybot import easyBot
from modes.regular import regularGame
from modes.extreme import extremeBot



def main():
	# Greetings 
	print("Welcome to the game of Stone, Paper, Scissor!")
	print("GAME MODES:")
	print("1. EasyBot(Scoring probability is 75%)")
	print("2. Regular Game")
	print("3. Extreme Difficulty(Scoring probability is 10%)\nNOTE: Every mode except 'Regular Game' allows you to use admin commands.")

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
		easyBot()
	elif ch==2:
		regularGame()
	elif ch==3:
		extremeBot()

	

if __name__ == "__main__":
	main()