import os

class ATM:

    def __init__(self, balance=0, pin_directory=None):
        self.balance = balance
        self.pin_directory = pin_directory
        self.pin = self.read_pin()  # Read PIN from file
        if not self.pin:
            print("Error: PIN not found or invalid. Please ensure 'pin.txt' contains a valid PIN.")
        self.update_file()  # Update the account balance file when creating a new ATM object

    def read_pin(self):
        try:
            # Read PIN from text file in the specified directory
            pin_file_path = os.path.join(self.pin_directory, "pin.txt")
            with open(pin_file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            print("Error: pin.txt file not found.")
            return ""

    def update_file(self):
        # Update the account balance file with the current balance
        with open("account_balance.txt", "w") as file:
            file.write(f"Current Balance: ${self.balance}")

    def verify_pin(self, entered_pin):
        # Verify if the entered PIN matches the stored PIN
        return entered_pin == self.pin

    def check_balance(self):
        # Display the current balance and update the account balance file
        print(f"Current Balance: ${self.balance}")
        self.update_file()

    def deposit(self, amount):
        # Deposit money into the account, update balance, print confirmation, and update the file
        self.balance += amount
        print(f"${amount} deposited successfully.")
        self.update_file()

    def withdraw(self, amount):
        # Withdraw money from the account if sufficient balance, else display error message
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.update_file()

def main():
    pin_directory = input("Enter the directory path where 'pin.txt' is located: ")

    # Initialize ATM object with starting balance of $100 and user-specified pin directory
    atm = ATM(100, pin_directory)

    if not atm.pin:
        return

    # Ask for PIN verification before allowing any operation
    while True:
        entered_pin = input("Enter PIN: ")
        if atm.verify_pin(entered_pin):
            print("PIN verification successful. You can now proceed.")
            break
        else:
            print("Incorrect PIN. Please try again.")

    while True:
        print("\nATM")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an operation: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = input("Enter amount to deposit: ")
            if amount.isdigit():
                atm.deposit(float(amount))
            else:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "3":
            amount = input("Enter amount to withdraw: ")
            if amount.isdigit():
                atm.withdraw(float(amount))
            else:
                print("Invalid input. Please enter a valid amount.")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()
