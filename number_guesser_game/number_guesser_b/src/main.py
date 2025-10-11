from src.utils.input_validator import get_valid_input
from src.game_logic.hint_generator import provide_hint
from src.game_logic.number_generator import generate_random_number
from src.game_logic.scorer import Scorer

def main():
    number_to_guess = generate_random_number(1, 100)
    scorer = Scorer()
    
    while True: 
        guess = get_valid_input(1, 100)
        if guess == number_to_guess:
            print(f"Congratulation. You guessed correctly.")
            print(f"You gained {scorer.get_score()}")
            break
        else:
            provide_hint(guess, number_to_guess)
            scorer.decrement_score()
    
if __name__ == "__main__":
    main()
