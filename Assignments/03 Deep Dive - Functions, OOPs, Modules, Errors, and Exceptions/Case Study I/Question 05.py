"""
Design software for bank systems. There should be options like cash withdrawal, 
cash credit, and a change password. According to user input, the software should 
provide the required output.
"""

class Bank:

    class UserAccount:
        def __init__(self, account_number, first_name, last_name, initial_deposit):
            self.account_number = account_number
            self.first_name = first_name
            self.last_name = last_name
            self.balance = initial_deposit

    def __init__(self):
        self.name = "Python Bank"
        self.accounts = {}

    def open_account(self, first_name, last_name, initial_deposit):
        new_account_number = len(self.accounts.keys()) + 1
        self.accounts[new_account_number] = self.UserAccount(
            new_account_number,
            first_name,
            last_name,
            initial_deposit
        )
        return new_account_number

    def account_exists(self, account_number):
        return account_number in self.accounts
    
    def deposit(self, account_number, amount):
        if not self.account_exists(account_number):
            return False
        current_balance = self.accounts[account_number].balance
        new_balance = current_balance + amount
        self.accounts[account_number].balance = new_balance
        return True
    
    def withdraw(self, account_number, amount):
        if not self.account_exists(account_number):
            return False
        current_balance = self.accounts[account_number].balance
        new_balance = current_balance - amount
        if new_balance < 0.0:
            return False
        self.accounts[account_number].balance = new_balance
        return True
    
    def transfer(self, from_account_number, to_account_number, amount):
        if not (self.account_exists(from_account_number) or self.account_exists(to_account_number)):
            return False
        from_account_current_balance = self.accounts[from_account_number].balance
        new_balance = from_account_current_balance - amount
        if amount < 0.0:
            return False
        self.accounts[from_account_number].balance = new_balance
        self.accounts[to_account_number].balance += amount
        return True

    def get_balance(self, account_number):
        if self.account_exists(account_number):
            return self.accounts[account_number].balance
        return -1.0


if __name__ == '__main__':
    bank = Bank()
    print("Welcome to", bank.name)
    while True:
        choice = int(input((
            "Available Services\n"
            "1. Open Bank Account\n"
            "2. Deposit Money\n"
            "3. Withdraw Money\n"
            "4. Transfer Money\n"
            "5. Know balance\n"
            "6. Exit\n"
            "Your Choice: "
        )))

        if choice == 1:
            f_name = input("First Name: ")
            l_name = input("Last Name: ")
            initial_deposit = float(input("Initial Deposit: "))
            account_number = bank.open_account(f_name, l_name, initial_deposit)
            print("New Account Number:", account_number)
        
        elif choice == 2:
            account_number = int(input("Account Number: "))
            amount = float(input("Enter deposit amount: "))
            deposited = bank.deposit(account_number, amount)
            if deposited:
                print(f"Money deposited. New balance is: {bank.get_balance(account_number):.3f}")
            else:
                print("Failed to deposit !!")
        
        elif choice == 3:
            account_number = int(input("Account Number: "))
            amount = float(input("Enter withdraw amount: "))
            withdrawn = bank.withdraw(account_number, amount)
            if withdrawn:
                print(f"Money Withdrawn. New balance is: {bank.get_balance(account_number):.3f}")
            else:
                print("Failed to withdraw !!")

        elif choice == 4:
            from_account_number = int(input("From Account Number: "))
            to_account_number = int(input("To Account Number: "))
            amount = float(input("Enter transfer amount: "))
            transferred = bank.transfer(from_account_number, to_account_number, amount)
            if transferred:
                print(f"Transfer successful, New balance for FROM account is: {bank.get_balance(from_account_number):.3f}")
            else:
                print("Transfer Failed !!")

        elif choice == 5:
            account_number = int(input("Account Number: "))
            balance = bank.get_balance(account_number)
            if balance > 0:
                print(f"Current Balance: {balance:.3f}")
            else:
                print("Invalid Account Number !!")

        elif choice == 6:
            exit(0)

        else:
            print("Invalid Choice !!")