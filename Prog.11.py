# Temperature Converter

# Welcome message
print("Welcome to the Temperature Converter!")

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Menu for conversion
print("\nChoose a conversion option:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Take user's choice
choice = input("\nEnter your choice (1 or 2): ")

if choice == '1':  # Celsius to Fahrenheit
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
elif choice == '2':  # Fahrenheit to Celsius
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
else:
    print("Invalid choice! Please select 1 or 2.")

# Goodbye message
print("\nThank you for using the Temperature Converter!")
