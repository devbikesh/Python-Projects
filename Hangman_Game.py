import random
hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]
words = ["python", "computer", "security", "network", "hacker"]
while True:
    secret_word = random.choice(words)
    hidden_word = []
    for character in secret_word:
        hidden_word.append("_")
    guessed_letters = []
    attempts = 6
    print("\n===== HANGMAN GAME =====")
    while attempts >0 and "_" in hidden_word:
        print(hangman_stages[6 - attempts])
        print("Word: " + " ".join(hidden_word))
        print("Guessed letters: " + ", ".join(guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print("Correct guess!")
            for index, character in enumerate(secret_word):
                if character == guess:
                    hidden_word[index] = guess
        else:
            print("Incorrect guess.")
            attempts -= 1
    if "_" not in hidden_word:
        print(hangman_stages[6 - attempts])
        print("🎉 You won!")
        print("The word was:", secret_word)
    else:
        print(hangman_stages[6])
        print("💀 You lost!")
        print("The word was:", secret_word)
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye!")
        break

