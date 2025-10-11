import random

class RockPaperScissors:
    """Main class for Rock Paper Scissors."""
    def __init__(self, name: str):
        self.choices = ["rock", "paper", "scissors"]
        self.name = name
        
    def get_player_choice(self):
        user_choice: str= input(f"Enter your choice ({self.choices}): ")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        print(f"Invalid choice. You must select from {self.choices}.")     
    
    def get_computer_choice(self):
        """To get computer choice randomly from choices."""
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """Decide winner based on choices."""
        if user_choice == computer_choice:
            return "No winner, it's a tie."
        
        win_combinations = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]
        for win_combination in win_combinations:
            if (user_choice == win_combination[0]) and (computer_choice == win_combination[1]):
                return f"Congratulation {self.name} won."
                  
        return "Sorry, the computer won!"
    
    def play(self):
        """Play the game.
        - Get the player choice.
        - Get the computer choice.
        - Decide the winner.
        - Print the result.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(self.decide_winner(user_choice, computer_choice))
        print(f"Computer choice: {computer_choice}")
        print(f"User choice: {user_choice}")
        
if __name__ == '__main__':
    game = RockPaperScissors("Parissa")
    
while True:
    game.play()
    
    continue_game = input("Wanna play again?! Enter 'q' to exit... ")
    if continue_game.lower() == "q":
        break        
        