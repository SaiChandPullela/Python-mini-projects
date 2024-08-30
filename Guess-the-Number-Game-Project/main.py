#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
# from replit import clear
from art import logo


def number():
    return random.randint(1, 100)


def compare(guess, number):
    if guess == number:
        print('You got it')
    elif guess > number:
        print('Too high')
    elif guess < number:
        print('Too low')


def play_game():
    print(logo)
    print('welcome to the number guessing game')
    print('I am thinking of a number between 1 and 100')
    game_end = False
    number_to_guess = number()
    attempts = 0
    difficulty = input('Choose a difficulty. Type "easy" or "hard": ').lower()
    if difficulty == 'easy':
        attempts += 10
        print(f'You have {attempts} attempts, Good Luck!')
    elif difficulty == 'hard':
        attempts += 5
        print(f'You have {attempts} attempts Good Luck!')
    else:
        print('Invalid input')
    while not game_end:
        guess = int(input('Make a guess: '))
        compare(guess, number_to_guess)
        attempts -= 1
        if guess == number_to_guess:
            print('You win')
            game_end = True
        elif attempts == 0:
            print(
                f'You are out of attempts, You loose\n the number is {number_to_guess}'
            )
            game_end = True
        else:
            print(f'You have {attempts} attempts left, go on!')


while input('Do you want to play a game of Guess the Number? Type "y" or "n": '
            ).lower() == 'y':
    # clear()
    play_game()
