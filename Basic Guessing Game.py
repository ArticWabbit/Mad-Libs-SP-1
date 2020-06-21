import os
os.system("cls")

# Title and Header
print("\u001b[32m~Basic Guessing game~")
print("---------------------\n")
print("Keep Typing Until You Get It Right\n")

# Variables
secret_word = "attention"
guessed_word = ""
guess_counter = 0

# Loop function
while guessed_word != secret_word:
    guessed_word = input("\u001b[37mGuess: ")
    if guessed_word != secret_word:
        guess_counter += 1
    else:
        print("\n\u001b[32mUnlocked\n")
        print("total guesses: " + str(guess_counter))

# Exit Prompt
input("\nPress ENTER to exit")
