# Armstrong Number Checker

# Welcome message
print("Welcome to the Armstrong Number Checker!")

# Take user input
number = int(input("Enter a number to check if it's an Armstrong number: "))

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    digits = list(map(int, str(num)))  # Convert number to list of digits
    power = len(digits)  # Get the number of digits
    return num == sum([digit ** power for digit in digits])  # Check Armstrong condition

# Check and display result
if is_armstrong(number):
    print(f"{number} is an Armstrong number!")
else:
    print(f"{number} is not an Armstrong number.")

# Goodbye message
print("\nThank you for using the Armstrong Number Checker!")
