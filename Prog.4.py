import random

print("Welcome to the Number Guessing Game!")

secret_number = random.randint(1, 100)
attempts = 0

print("\nI have chosen a number between 1 and 100. Can you guess it?")

while True:
    attempts += 1

    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break

print("\nThanks for playing the Number Guessing Game!")
