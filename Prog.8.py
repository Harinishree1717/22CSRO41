# Factorial Calculator

# Welcome message
print("Welcome to the Factorial Calculator!")

# Take user input
num = int(input("Enter a non-negative integer to calculate its factorial: "))

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case: 0! and 1! = 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Calculate and display the factorial
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")

# Goodbye message
print("\nThank you for using the Factorial Calculator!")
