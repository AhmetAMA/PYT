import random
import time

# Variables
words = ["ace", "dog", "speed", "truck", "room", "stage", "levels", "supercalifragilisticexpialidocious"]
word = random.choice(words)
lives = 6
guessed = ""
blanks = ["_"] * len(word)

# Intro
tutorial = input("Would you like a tutorial? (y/n)\n ===>  ")
if str.lower(tutorial) == "y":
    print("Hello! Welcome to my hangman game!")
    time.sleep(2)
    print("The game works as follows:")
    time.sleep(3)
    print("Every round, a random word is selected.")
    time.sleep(3)
    print("You have to guess the word, one letter at a time.")
    time.sleep(3)
    print("Every time you correctly guess a letter, its position in the word is revealed.")
    time.sleep(3)
    print("However, when you incorrectly guess a letter, you will lose a life.")
    time.sleep(4)
    print("You have 6 lives, and your only hints are the length of the word, and your own inputs.")
    time.sleep(4)
    print("You can type 'quit' to exit the game.")
    time.sleep(3)
    print("Good luck, have fun!")
    time.sleep(2.5)
else:
    print("\n\n\n\n\n\n\n")
# Loops until player is out of lives
while lives > 0:

    # For debugging purposes
    print('Word Length: '+str(len(word))+'')
    #print('Current word: "'+str(word)+'"')
    print('Lives: '+str(lives)+'')
    print('Guessed letters: "' +str(guessed)+'"')

    # Main game

    if "_" not in blanks:
        if word == "dog":
            print("\n\nWhat the dog doing?")
        print("You won! The word was "+ word +"!\n Would you like to play again?")
        again = input("Y/N?\n")
        if str.lower(again) == "y":
            lives = 6
            word = random.choice(words)
            blanks = ["_"] * len(word)
            guessed = ""
        elif str.lower(again) == "n":
            print("Thanks for playing!")
            time.sleep(1)
            break
    print("\n\nWord:")
    print("".join(blanks))
    guess = input("Guess a letter:\n")
    if len(guess) != 1 and guess != "quit":
        print("\n\nYou can only enter one letter!")
    elif str.lower(guess) == "quit":
        print("\n\nQuitting game!")
        time.sleep(2)
        break

    while len(guess) == 1:

        # Simply checks if the guessed letter is in the word.
        if guess in word:
            if guess in guessed:
                print("\n\nYou already guessed the letter, " +guess+"!")
                break
            print('\n\nCorrect, the letter "' + guess + '" is in the word!')
            guessed = guessed + guess
            for i, letter in enumerate(word):
                if letter != "_" and guess == letter:
                    blanks[i] = letter
            break
        elif guess not in word:
            guessed = guessed + guess
            lives -= 1
            print('\n\nIncorrect, the letter "' + str(guess) + '" is not in the word.\n You have '+str(lives)+' lives left.')
            break 
        else:
            guessed = guessed + guess
            lives -= 1
            print('\n\nIncorrect, the letter "' + str(guess) + '" is not in the word.\n You have '+str(lives)+' lives left.')
            break 

    if str(blanks) == word:
        if word == "dog":
            print("\n\nWhat the dog doing?")
        print("You won! The word was "+ word +"!\n Would you like to play again?")
        again = input("Y/N?\n")
        if str.lower(again) == "y":
            lives = 6
            word = random.choice(words)
            guessed = ""
        elif str.lower(again) == "n":
            print("Thanks for playing!")
            time.sleep(1)
            break

    elif lives == 0:
        print("\n")
        print('Game over! The word was: "' + word + '". Would you like to play again?\n')
        again = input("Y/N?\n")
        if str.lower(again) == "y":
            lives = 6
            word = random.choice(words)
            guessed = ""
            blanks = ["_"] * len(word)
        elif str.lower(again) == "n":
            print("Thanks for playing!")
            time.sleep(1)
            break
        else:
            quit()