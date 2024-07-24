import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number!")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        # Get the player's guess
        guess = input("Enter your guess: ")

        # Validate input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        # Convert the guess to an integer
        guess = int(guess)
        number_of_guesses += 1

        # Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {number_of_guesses} tries.")
            break

if __name__ == "__main__":
    guessing_game()
