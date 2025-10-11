import random


def validate_input(user_guess):
    # check if user's input is numeric
    if not user_guess.isdigit():
        print("Invalid input. Please enter a number.")
        return False
    
    # convert to integer after confirming it's digits
    user_guess = int(user_guess)
    # check if user's guess is in valid range
    if user_guess < 1 or user_guess > 100:
        print("Your guess is out of range. Enter a number from 1 to 100.")
        return False
    
    return True


def main():
    # Generate a random number between 1 and 100 (inclusive)
    rand_num = random.randint(1, 100)
    print(f"the secret number is: {rand_num}")
    attempts = 0

    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        # Allow quitting the game
        if user_guess == "q":
            print("Thank you for playing. Goodbye.")
            break
        
        # Validate input, continue loop if invalid
        if not validate_input(user_guess):
            continue
    
        # Check user guess against the random number
        user_guess = int(user_guess)
        if user_guess == rand_num:
            print(f"Congratulation. Your guess is just right. You attempted: {attempts}")
            break  
        elif rand_num > user_guess:
            print("Your guess is too low.")
        elif rand_num < user_guess:
            print("Your guess is too high.")

        # Increment attempts at the end of the loop
        attempts += 1
        
if __name__ == "__main__":
    main()
    