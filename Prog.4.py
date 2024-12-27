import random

# Welcome message
print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("\nI have chosen a number between 1 and 100. Can you guess it?")

# Game loop
while True:
    # Increment the attempt counter
    attempts += 1

    # Take the user's guess
    guess = int(input("Enter your guess: "))

    # Check the guess
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break

# Goodbye message
print("\nThanks for playing the Number Guessing Game!")
