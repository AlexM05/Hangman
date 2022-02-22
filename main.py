import random
import os
HANGMANPICS = ['''''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def clearConsole():
    command = ''
    if os.name == 'nt':
        command = 'cls'
    elif os.name == 'dos':
        command = 'clear'
    os.system(command)

def main():
    while True:

        query = input("Do you want a easy or hard game?: ")
        Fl = query[0].lower()
        i = 1
        if query == '' or not Fl in ['h', 'e']:
            print('Please answer with easy or hard!')
            query = input("Do you want a easy or hard game?: ")
        elif Fl == 'h':

            with open('hard.txt', 'r') as f:
                words = f.readlines()

            word = random.choice(words)[:-1]

            allowed_errors = 6
            guesses = []
            done = False

            while not done:
                for letter in word:
                    if letter.lower() in guesses:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print("")
                done = True

                guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
                clearConsole()
                guesses.append(guess.lower())
                if guess.lower() not in word.lower():
                    allowed_errors -= 1
                    print(HANGMANPICS[i])
                    i += 1
                if allowed_errors == 0:
                    break

                done = True
                for letter in word:
                    if letter.lower() not in guesses:
                        done = False

            if done:
                print(f"Game Over! The word was {word}!")
                input('Press Any Key to Exit: ')
                break

        elif Fl == 'e':

            with open('easy.txt', 'r') as f:
                words = f.readlines()

            word = random.choice(words)[:-1]

            allowed_errors = 6
            guesses = []
            done = False

            while not done:
                for letter in word:
                    if letter.lower() in guesses:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                print("")
                done = True

                guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
                clearConsole()
                guesses.append(guess.lower())
                if guess.lower() not in word.lower():
                    allowed_errors -= 1
                    print(HANGMANPICS[i])
                    i += 1
                if allowed_errors == 0:
                    break

                done = True
                for letter in word:
                    if letter.lower() not in guesses:
                        done = False

            if done:
                if i < 5:
                    print("YOU FOUND THE WORD!!!")
                else:
                    print(f"Game Over! The word was {word}!")
                restart_input = input("Would you like to play again? ")
                restart = restart_input[0].lower()
                if restart == "y":
                    main()
                elif restart == "n":
                    break
                break

if __name__ == "__main__":
    main()