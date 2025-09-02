from custom import logo
import random

GAME_LEVEL_EASY = 10
GAME_LEVEL_HARD = 5

def choose_level():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        return GAME_LEVEL_EASY
    else:
        return GAME_LEVEL_HARD

print(logo)

answer = random.randint(1, 100)
print(f"Correct Answer: {answer}")

def guess_the_number():
    global attempts
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print("You got it!")
            return
        elif guess > answer:
            print("Too high!")
            attempts -= 1
        elif guess < answer:
            print("Too low!")
            attempts -= 1
    print(f"Sorry, the number was {answer}.")

attempts = choose_level()

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


guess_the_number()

