import random
import utils as u

def cheatsCheck(cmd: str, user: int, comp: int) -> tuple[int, int]:
	"""
	Checks if the command is an admin command and applies it.
	"""
	if cmd.isdigit() and int(cmd) in [1, 2, 3]:
		return int(cmd), comp # Proceed game normally
	
	elif cmd == "adminImmortal":
		return u.adminImmortal(user, comp) # Apply Immortal command
	
	else:
		return cmd, comp # Invalid command, return unchanged values
		

def main():
	# Greetings 
	print("Welcome to the game of Stone, Paper, Scissor!")
	print("You can enter your choice as a number (1 for stone, 2 for paper, 3 for scissor) or use commands like 'adminImmortal' to cheat.")
	options = {1: "stone", 2: "paper", 3: "scissor"}
	commands = ["adminImmortal", 'fyou']

	# User and Computer Scores
	compS=0
	userS=0
	# User and Computer choices
	user = -1
	comp = -1

	# Main game loop
	while compS<5 and userS<5:
		
		ch = input(f"Enter your choice: ")
		comp=random.choice(list(options.keys()))
		user, comp = cheatsCheck(ch, user, comp)


		# If choice is not valid(neither a number nor a command) 
		if user not in [1, 2, 3] and user not in commands:
			print(f"Choose from these options: {options}")
			continue

		print(f"Computer's choice: {options[comp]}\tYour choice: {options[user]}")
		if user==comp:
			print("Its a tie! ")
		elif (user==1 and comp== 3) or (user==2 and comp==1) or (user==3 and comp==2):
			print("You Scored !!!!")
			userS += 1

		elif (user==3 and comp==1) or (user==2 and comp==3) or (user==1 and comp==2):
			print("Computer Scored !!!!!")
			compS+=1
		print(f"compSuter score: {compS} \t User score: {userS}")

	# Check for game end
	if compS==5 : 
		print("Computer WON !!! ")
	else :
		print("tu jit gya ladlee !!!") 

if __name__ == "__main__":
	main()