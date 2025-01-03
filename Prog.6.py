# Palindrome Checker

# Welcome message
print("Welcome to the Palindrome Checker!")

# Take user input
user_input = input("Enter a word or phrase to check if it's a palindrome: ")

# Function to check if the string is a palindrome
def is_palindrome(text):
    # Remove spaces and convert to lowercase for comparison
    cleaned_text = ''.join(filter(str.isalnum, text)).lower()
    # Check if the cleaned text is the same as its reverse
    return cleaned_text == cleaned_text[::-1]

# Check and display result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")

# Goodbye message
print("\nThank you for using the Palindrome Checker!")
