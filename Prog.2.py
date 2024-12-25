# Simple Calculator Program

# Welcome message
print("Welcome to the Simple Calculator!")

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Menu for operations
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Taking the user's choice
choice = input("\nEnter the number corresponding to your choice: ")


if choice == '1':
    print(f"The result of addition is: {num1 + num2}")
elif choice == '2':
    print(f"The result of subtraction is: {num1 - num2}")
elif choice == '3':
    print(f"The result of multiplication is: {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"The result of division is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please select a valid operation.")

# Goodbye message
print("\nThank you for using the Simple Calculator!")
