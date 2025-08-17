import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

WIN_SCORE = 11
options = {'1': "stone", '2': "paper", '3': "scissor"}
commands = ["adminImmortal", 'adminFyou']
win_messages = {
    "easy": f"{Fore.WHITE}{Back.GREEN}tu jit gya ladlee\t\n{Style.RESET_ALL}Koi badi baat nhi h ye " + f"{Fore.YELLOW}{Back.BLACK}XD{Style.RESET_ALL}",
    "regular": f"{Fore.WHITE}{Back.GREEN}tu jit gya ladlee\t{Style.RESET_ALL}",
    "hard": f"{Fore.WHITE}{Back.GREEN}tu jit gya ladlee\n{Style.RESET_ALL}Luck bhari h aaj tera!!!"
}
lose_messages = {
    "easy": f"{Fore.WHITE}{Back.RED}Computer WON!!\nEasyBot se haar gya chomu {Style.RESET_ALL}" + f"{Fore.YELLOW}{Back.BLACK}XD{Style.RESET_ALL}",
    "regular": f"{Fore.WHITE}{Back.RED}Computer WON!!\nKoi baat nhi, agle baar jeet jayega! {Style.RESET_ALL}" + f"{Fore.YELLOW}{Back.BLACK}:){Style.RESET_ALL}",
    "hard": f"{Fore.WHITE}{Back.RED}Computer WON!!\nKaidee me rahiyee Chhotee, Wrna g*nd pe lagenge sotteee!!!\t{Style.RESET_ALL}"
}


def admin_immortal() -> tuple[int, int]:
    return "1", "3"


def admin_f_you() -> tuple[int, int]:
    return "2", "3"


def print_rules():
    """
    Prints the rules of the game.
    """
    print(f"{Fore.RED}R{Fore.BLUE}U{Fore.GREEN}L{Fore.MAGENTA}E{Fore.YELLOW}S:")
    print("1.You can enter your choice as a number (1 for stone, 2 for paper, 3 for scissor).")
    print("2. First to score 11 points wins the game.")


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
    

def update_scores(user: str, comp: str, user_score: int, comp_score: int) -> tuple[int, int]:
    """
    Checks who has got this point based on their choices.
    """
    if user == comp:
        print(f"{Fore.YELLOW}{Back.BLACK}Its a tie! ")
    elif (user == "1" and comp == "3") or (user == "2" and comp == "1") or (user == "3" and comp == "2"):
        print(f"{Fore.GREEN}{Back.BLACK}You Scored !!!!")
        user_score += 1
    elif (user == "3" and comp == "1") or (user == "2" and comp == "3") or (user == "1" and comp == "2"):
        print(f"{Fore.RED}{Back.BLACK}Computer Scored !!!!!")
        comp_score += 1

    return user_score, comp_score


def check_winner(comp_score: int, user_score: int, game_mode: str) -> None:
    """
    Checks who has won the game based on the scores.
    """
    if comp_score == WIN_SCORE:
        print(lose_messages[game_mode])
    elif user_score == WIN_SCORE:
        print(win_messages[game_mode])