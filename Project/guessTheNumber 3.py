import random  # Import the random module to generate random numbers

def guess_number():
    # Function to play the number guessing game
    while True:
        try:
            # Ask the user to input the range for the random number
            min_range = int(input("Enter the minimum number of the range: "))
            max_range = int(input("Enter the maximum number of the range: "))
            
            if min_range > max_range:
                print("Invalid input. Minimum range should be less than or equal to the maximum range.")
                continue

            break
        except ValueError:
            # Handle the case where the user inputs non-integer values for the range
            print("Invalid input. Please enter valid integers for the range.")

    # Generate a random target number within the specified range
    target_number = random.randint(min_range, max_range)
    attempts = 0  # Initialize the attempts counter

    print(f"Guess the number between {min_range} and {max_range}.")

    # Start the game loop
    while True:
        attempts += 1  # Increment the attempts counter

        while True:
            try:
                # Ask the user to input their guess
                user_guess = int(input(f"Attempt {attempts}: Enter your guess: "))
                break
            except ValueError:
                # Handle the case where the user inputs a non-integer guess
                print("Invalid input. Please enter a valid integer.")

        # Check if the user's guess is correct
        if user_guess < target_number:
            print("Higher!")  # Inform the user to guess higher
            min_range = user_guess + 1  # Adjust the minimum range for the next guess
        elif user_guess > target_number:
            print("Lower!")  # Inform the user to guess lower
            max_range = user_guess - 1  # Adjust the maximum range for the next guess
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts!")
            break  # End the game if the user guesses correctly

    # Ask the user if they want to play again
    while True:
        try:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again not in ['yes', 'no']:
                raise ValueError
            break
        except ValueError:
            # Handle the case where the user inputs an invalid choice
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Restart the game if the user chooses to play again, otherwise exit
    if play_again == "yes":
        guess_number()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    guess_number()
