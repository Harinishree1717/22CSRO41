# Multiplication Table Generator

# Welcome message
print("Welcome to the Multiplication Table Generator!")

# Taking input from the user
number = int(input("Enter a number to generate its multiplication table: "))

# Display the multiplication table
print(f"\nMultiplication Table for {number}:\n")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Goodbye message
print("\nThank you for using the Multiplication Table Generator!")
