# Number Guesser Game Project
## Description:
This project is a game where the user must guess a number between 1 and 100. The program generates a random number. Then, the user enters a guess. For each incorrect attempt, the user receives a hint. In addition, their score decreases by 10 for every wrong guess.

### Tips:
- src/main.py: The main entry point of the game. It handles the game loop, user input, and display.
- src/game_logic/: Contains the core game logic.
  - number_generator.py: Generates a random number.
  - hint_generator.py: Provides hints based on the user's guess.
  - scorer.py: Manages the scoring system.
  - src/utils/: Contains utility functions.
  - input_validator.py: Validates user input.

### How to run:
run `pip install -r requirement.txt` in your command line,
then run `python main.py` 
