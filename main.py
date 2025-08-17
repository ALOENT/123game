import colorama
from colorama import Fore, Back, Style
from modes.easybot import easy_bot
from modes.regular import regular_game
from modes.extreme import extreme_bot
colorama.init(autoreset=True)


def main():
    # Greetings 
    # from colorama import Fore, Back, Style
    print(f"{Fore.YELLOW}{Back.BLACK}:){Style.RESET_ALL}")
    print(Back.BLUE+Fore.GREEN+"Welcome to the game of Stone, Paper, Scissor!")

    while True:
        # Game mode selection
        while True:
            print("GAME MODES:")
            print(f"1.{Fore.CYAN} EasyBot(Scoring probability is 75%)")
            print(f"2.{Fore.YELLOW} Regular Game")
            print(f"3.{Fore.RED} Extreme Difficulty(Scoring probability is 10%)")
            print(f"{Fore.WHITE}{Back.BLACK}NOTE: Every mode except 'Regular Game' allows you to use admin commands.")
            ch = input("Enter game mode(1, 2 or 3): ")
            if ch not in ['1', '2', '3']:
                print(f"{Fore.RED}Invalid choice! Please choose a valid game mode.")
                continue
            break

        # Play the selected mode
        if ch == '1':
            easy_bot()
        elif ch == '2':
            regular_game()
        elif ch == '3':
            extreme_bot()

        # Replay option
        while True:
            play_again = input(f"Do you want to play again? ({Fore.GREEN}y/{Fore.RED}n{Fore.WHITE}): ").strip().lower()
            if play_again not in ['y', 'n']:
                print(f"{Fore.RED}Invalid choice! Please enter 'y' or 'n'.")
                continue
            break

        if play_again == 'n':
            print(f"{Fore.GREEN}Thank you for playing! Goodbye!")
            break


if __name__ == "__main__":

    main()