import random

WIN_SCORE = 11
options = {'1': "stone", '2': "paper", '3': "scissor"}
commands = ["adminImmortal", 'adminFyou']


def admin_immortal() -> tuple[int, int]:
    return "1", "3"


def admin_f_you() -> tuple[int, int]:
    return "2", "3"


def print_rules():
    """
    Prints the rules of the game.
    """
    print("RULES:\n1.You can enter your choice as a number (1 for stone, 2 for paper, 3 for scissor).\n2. First to score 11 points wins the game.")


def comp_prob_easy(userC: int) -> int:
    """
    This function selects the computer's move with a 75% probability that favors the user’s victory and a 25% probability for either a draw or the computer’s victory.
    """
    choices = list(options.keys())
    
    if userC == "1":
        weights = [0.125, 0.125, 0.75]
    elif userC == "2":
        weights = [0.125, 0.75, 0.125]
    elif userC == "3":
        weights = [0.75, 0.125, 0.125]

    comp = random.choices(choices, weights=weights, k=1)[0]
    return comp


def comp_prob_hard(userC: str) -> str:
    """
    This function selects the computer's move with a 90% probability that favors the user’s defeat and a 10% probability for either a draw or the computer’s defeat.
    """
    choices = list(options.keys())
    
    if userC == "1":
        weights = [0.05, 0.90, 0.05]
    elif userC == "2":
        weights = [0.05, 0.05, 0.90]
    elif userC == "3":
        weights = [0.90, 0.05, 0.05]

    comp = random.choices(choices, weights=weights, k=1)[0]
    return comp


def cheats_check(cmd: str, lev: str) -> tuple[str, str]:
    """
    Checks if the command is an admin command and applies it.
    """
    if cmd in list(options.keys()):
        if lev == "easy":
            return cmd, comp_prob_easy(cmd) # Use easy bot's probability logic
        elif lev == "hard":
            return cmd, comp_prob_hard(cmd)  # Use extreme bot's probability logic
     
    elif cmd == "adminImmortal":
        return admin_immortal() # Apply Immortal command
    
    elif cmd == "adminFyou":
        return admin_f_you() # Apply Fyou command
	
    else:
    	return cmd, "-1" # Invalid command, return unchanged values