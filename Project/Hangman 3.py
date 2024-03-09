import random  # Import the random module to generate random words

def choose_word():
    # Function to choose a word for the Hangman game
    print("Guess the last name of a famous writer")
    word_list = ["chavchavadze", "aligieri", "chiladze", "dochanashvili", "murakami", "eco"]
    return random.choice(word_list)  # Choose a random word from the list

def display_word(word, guessed_letters):
    # Function to display the word with correctly guessed letters and underscores for unguessed letters
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter  # If the letter has been guessed, display it
        else:
            display += "_"  # If the letter hasn't been guessed, display an underscore
    return display

def hangman():
    # Function to play the Hangman game
    word = choose_word()  # Choose a word for the game
    max_attempts = 6  # Maximum number of incorrect guesses allowed
    guessed_letters = []  # List to store guessed letters
    attempts = 0  # Counter for the number of attempts made
    
    print("Welcome to Hangman!")
    print("The word contains", len(word), "letters.")
    
    while True:
        print("\nWord:", display_word(word, guessed_letters))  # Display the word with guessed letters
        try:
            guess = input("Guess a letter: ").lower()  # Get the user's guess and convert it to lowercase
            if not guess.isalpha() or len(guess) != 1:
                raise ValueError("Please enter a single letter.")  # Check if the input is a single letter
        except ValueError as ve:
            print(ve)  # Print the error message if the input is invalid
            continue  # Skip to the next iteration of the loop
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")  # Check if the letter has already been guessed
            continue  # Skip to the next iteration of the loop
        
        guessed_letters.append(guess)  # Add the guessed letter to the list
        
        if guess in word:
            print("Correct!")  # Check if the guess is correct
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You guessed the word:", word)
                break  # End the game if the word has been fully guessed
        else:
            attempts += 1  # Increment the number of attempts made
            print("Incorrect guess. Attempts left:", max_attempts - attempts)  # Inform the user about remaining attempts
            if attempts == max_attempts:
                print("You've run out of attempts. The word was:", word)
                break  # End the game if the maximum number of attempts has been reached

    play_again = input("Do you want to play again? (yes/no): ").lower()  # Ask the user if they want to play again
    if play_again == "yes":
        hangman()  # Restart the game if the user chooses to play again
    else:
        print("Thanks for playing!")  # Thank the user for playing if they choose not to play again

if __name__ == "__main__":
    hangman()
