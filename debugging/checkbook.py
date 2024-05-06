class Checkbook:
    def __init__(self):
        """
        Function Description:
        Initialize a Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Deposit the specified amount into the checkbook balance.

        Parameters:
        - amount: The amount to be deposited (float).
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        Withdraw the specified amount from the checkbook balance, if sufficient funds are available.

        Parameters:
        - amount: The amount to be withdrawn (float).
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        Retrieve and print the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Function Description:
    Main function to interact with the Checkbook object.

    Action:
    - Prompts the user for action (deposit, withdraw, balance, exit).
    - Handles user input and performs corresponding actions.
    - Exit the loop when the user chooses to exit.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
