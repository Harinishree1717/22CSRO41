# Fibonacci Sequence Generator

# Welcome message
print("Welcome to the Fibonacci Sequence Generator!")

# Take user input
n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))

# Function to generate Fibonacci sequence
def generate_fibonacci(terms):
    sequence = []
    a, b = 0, 1
    for _ in range(terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Generate and display the Fibonacci sequence
if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci(n)
    print(f"\nThe first {n} terms of the Fibonacci sequence are:")
    print(fibonacci_sequence)

# Goodbye message
print("\nThank you for using the Fibonacci Sequence Generator!")
