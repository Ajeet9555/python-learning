class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
            Hello, How would you like to proceed?
            1. Enter 1 to create PIN
            2. Enter 2 to deposit
            3. Enter 3 to withdraw
            4. Enter 4 to check balance
            5. Enter 5 to exit
            Enter your choice: """)
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("\nThank you for using our service.")
                break
            else:
                print("\nInvalid input. Please enter a number from 1 to 5.")

    def create_pin(self):
        self.pin = input("Enter your new PIN: ")
        if self.pin.isdigit() and len(self.pin) == 4:
            print("PIN created successfully.")
        else:
            print("PIN must be exactly 4 digits.")
            self.pin = ""

    def deposit(self):
        if self.pin == "":
            print("Please create a PIN first.")
            return
        temp_pin = input("Enter your PIN: ")
        if temp_pin == self.pin:
            try:
                amount = int(input("Enter the amount to deposit: "))
                if amount > 0:
                    self.balance += amount
                    print(
                        f"Amount deposited successfully. "
                        f"Your new balance is ₹{self.balance}"
                    )
                else:
                    print("Please enter an amount greater than 0.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        else:
            print("Invalid PIN. Please try again.")

    def withdraw(self):
        if self.pin == "":
            print("Please create a PIN first.")
            return
        temp_pin = input("Enter your PIN: ")
        if temp_pin == self.pin:
            try:
                amount = int(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Please enter an amount greater than 0.")
                elif amount <= self.balance:
                    self.balance -= amount
                    print(
                        f"Amount withdrawn successfully. "
                        f"Your new balance is ₹{self.balance}"
                    )
                else:
                    print("Insufficient balance.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        else:
            print("Invalid PIN. Please try again.")

    def check_balance(self):
        if self.pin == "":
            print("Please create a PIN first.")
            return
        temp_pin = input("Enter your PIN: ")
        if temp_pin == self.pin:
            print(f"Your current balance is ₹{self.balance}")
        else:
            print("Invalid PIN. Please try again.")

sbi = Atm()