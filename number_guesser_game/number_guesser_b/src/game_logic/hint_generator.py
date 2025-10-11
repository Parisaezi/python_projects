def provide_hint(guess, number_to_guess):
    if guess == number_to_guess:
        print("Congratulations! Your guess is just right.")
    elif guess < number_to_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
