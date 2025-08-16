import random
import utils as utils

def cheatsCheck(cmd: str) -> tuple[int, int]:
	"""
	Checks if the command is an admin command and applies it.
	"""
	if cmd in ["1", "2", "3"]:
		return int(cmd) # Proceed game normally
	
	elif cmd == "adminImmortal":
		return utils.adminImmortal(cmd) # Apply Immortal command
	
	elif cmd == "adminFyou":
		return utils.adminFyou(cmd) # Apply Fyou command
	
	else:
		return cmd # Invalid command, return unchanged values
	

def compProb(userC: int) -> int:
    """
    This function selects the computer's move with a 90% probability that favors the user’s defeat and a 10% probability for either a draw or the computer’s defeat.
    """
    choices = [1, 2, 3]
    if userC == 1:
        weights = [0.05, 0.90, 0.05]
    elif userC == 2:
        weights = [0.05, 0.05, 0.90]
    elif userC == 3:
        weights = [0.90, 0.05, 0.05]

    comp = random.choices(choices, weights=weights, k=1)[0]
    return comp


commands = ["adminImmortal", 'adminFyou']
def extremeBot():
	"""
	Function to play the extreme bot game with a 10% probability of scoring.
	"""
	print("------------------------------------------------------------------------")
	print("Starting ExtremeBot mode...")
	print("RULES:\n1.You can enter your choice as a number (1 for stone, 2 for paper, 3 for scissor).\n2. First to score 11 points wins the game.")

	options = {1: "stone", 2: "paper", 3: "scissor"}
	# User and Computer Scores
	compS=0
	userS=0
	
	# Main game loop
	while compS<11 and userS<11:
		try:
			user = input(f"Enter your choice: ")
			# If choice is not valid 
			if user not in ['1', '2', '3'] and user not in commands:
				print(f"Invalid choice!!!\nChoose from these options: {options}")
				continue
		except ValueError:
			print("Invalid input! Please enter a number (1, 2 or 3).")
			continue
		
		if user in commands:
			user, comp = cheatsCheck(user)
		else:
			comp = compProb(int(user))

		print(f"Computer's choice: {options[comp]}\tYour choice: {options[int(user)]}")
		if int(user)==comp:
			print("Its a tie! ")
		elif (int(user)==1 and comp== 3) or (int(user)==2 and comp==1) or (int(user)==3 and comp==2):
			print("You Scored !!!!")
			userS += 1

		elif (int(user)==3 and comp==1) or (int(user)==2 and comp==3) or (int(user)==1 and comp==2):
			print("Computer Scored !!!!!")
			compS+=1
		print(f"Computer's score: {compS} \t User's score: {userS}")
		print("-----------------------------------------------------------------------")

	# Check for game end
	if compS==11 : 
		print("Computer WON !!!\nKaidee me rahiyee Chhotee, Wrna g*nd pe lagenge sotteee!!!")
	else :
		print("tu jit gya ladlee\nLuck bhari h aaj tera!!!") 

	# Ask if the user wants to play again
	print("-----------------------------------------------------------------------")
	print("Game Over!")