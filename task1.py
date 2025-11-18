import random

def hangman():
    # List of possible words
    word_list = ["apple", "banana", "cherry", "orange", "grape"]

    # Pick a random word from the list
    secret_word = random.choice(word_list)

    # Keep track of guesses
    guessed = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print("_ " * len(secret_word))  # Show blanks for each letter

    # Main game loop
    while wrong_guesses < max_wrong:
        guess = input("Enter a letter: ").lower()

        # Make sure user enters one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please type a single letter.")
            continue

        # Check if user already guessed this letter
        if guess in guessed:
            print("You already tried that letter.")
            continue

        # Add guess to list
        guessed.append(guess)

        # Check if the letter is in the word
        if guess in secret_word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("Wrong letter. You have", max_wrong - wrong_guesses, "tries left.")

        # Build the word display
        shown_word = ""
        for letter in secret_word:
            if letter in guessed:
                shown_word += letter + " "
            else:
                shown_word += "_ "
        print(shown_word.strip())

        # Check if player has won
        all_found = True
        for letter in secret_word:
            if letter not in guessed:
                all_found = False
                break

        if all_found:
            print("You guessed the word! It was:", secret_word)
            break

    # If user runs out of guesses
    if wrong_guesses == max_wrong:
        print("You ran out of tries. The word was:", secret_word)

# Start the game

hangman()
