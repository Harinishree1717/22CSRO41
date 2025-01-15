# ATM Simulator

# Welcome message
print("Welcome to the ATM Simulator!")

# Initial balance
balance = 5000

# Display ATM options
def show_menu():
    print("\nMenu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# ATM Operations
while True:
    show_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':  # Check balance
        print(f"\nYour current balance is: ₹{balance}")
    
    elif choice == '2':  # Deposit money
        amount = float(input("Enter the amount to deposit: ₹"))
        if amount > 0:
            balance += amount
            print(f"₹{amount} has been deposited. New balance: ₹{balance}")
        else:
            print("Invalid amount. Please try again.")

    elif choice == '3':  # Withdraw money
        amount = float(input("Enter the amount to withdraw: ₹"))
        if 0 < amount <= balance:
            balance -= amount
            print(f"₹{amount} has been withdrawn. Remaining balance: ₹{balance}")
        else:
            print("Insufficient balance or invalid amount. Please try again.")
    
    elif choice == '4':  # Exit
        print("\nThank you for using the ATM Simulator! Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")
