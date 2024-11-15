# guessing_game.py
import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
guess = None
guesses = 0

while guess != number:
    guess = input("Take a guess: ")
    guesses += 1

    try:
        guess = int(guess)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print(f"Congratulations! You guessed the number in {guesses} guesses.")
