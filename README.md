# Rock Paper Scissors (Stone, Paper, Scissor) Game

A modular, Python-based command-line Rock-Paper-Scissors game with selectable difficulties and hidden admin commands. Challenge yourself against different AI strategies—from friendly to ruthless!

---

## Features

- **Three Game Modes:**
  - **EasyBot:** 75% chance to win each round.
  - **Regular Game:** Classic fair play.
  - **Extreme Difficulty:** 10% chance to win—try your luck!
- **Admin Commands:** Secret in-game codes to shake up the rules (try them in Easy and Extreme modes).
- Modular code organization for ease of maintenance and extension.

---

## Getting Started

### Requirements

- Python 3.7 or later

### Installation

1. **Clone this repository:**
git clone https://github.com/ALOENT/123game.git
cd 123game

2. **Run the game:**
python main.py

---

## How to Play

1. **Choose a Game Mode:**
- Enter `1` for EasyBot
- Enter `2` for Regular Game
- Enter `3` for Extreme Difficulty

2. **Enter Your Move:**
- Type `1` for Stone
- Type `2` for Paper
- Type `3` for Scissor

3. **First to 11 Points Wins!**

4. **Admin Commands (Easy & Extreme only):**
- `adminImmortal` or `adminFyou` (discover their effects!)

---

## File Structure

123game/
├── main.py               # Entry point, menu, and mode selection
├── utils.py              # Shared constants, rules, and utility functions
├── modes/
│   ├── easybot.py        # EasyBot mode logic
│   ├── regular.py        # Regular mode logic
│   └── extreme.py        # Extreme mode logic
└── README.md             # Project documentation


---

## Customization Ideas

- Change the `WIN_SCORE` in `utils.py` for longer or shorter matches.
- Expand with new modes or admin commands.

---

## Contributing

Pull requests welcomed! Please ensure code is modular, readable, and PEP 8 compliant.

---

## License

This project is open-source and free to use.

---

Enjoy the game, and good luck beating ExtremeBot!
