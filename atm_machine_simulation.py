class InsufficientFundsException(Exception):
    pass

class InvalidAmountException(Exception):
    pass

class CustomException:
    def __init__(self, balance_amount):
        self.balance_amount = balance_amount
    
    def balance(self):
        return self.balance_amount

    def withdraw(self, withdraw_amount):
        try:
            if withdraw_amount <= 0:
                raise InvalidAmountException
            elif self.balance_amount < withdraw_amount:
                raise InsufficientFundsException
            else:
                self.balance_amount -= withdraw_amount
                return self.balance_amount
        
        except InvalidAmountException:
            return "Enter a valid Amount"

        except InsufficientFundsException:
            return "Insufficient Balance in the Account"
        
    def deposit(self, deposit_amt):
        if deposit_amt < 0:
            return "Enter a valid amount to deposit"
        else:
            self.balance_amount += deposit_amt
            return self.balance_amount

    def atm_simulation(self):
        while True:
            print("Enter the number of the action to perform:")
            print("1. Withdraw")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Exit")
            action = int(input())
            if action == 1:
                withdraw_amt = int(input("Enter amount to Withdraw: "))
                new_balance = self.withdraw(withdraw_amt)
                print("Your Current Balance: ", new_balance)
            elif action == 2:
                print("Your Current Balance: ", self.balance_amount)
            elif action == 3:
                deposit_amt = int(input("Enter amount to Deposit: "))
                new_balance = self.deposit(deposit_amt)
                print("Your Current Balance: ", new_balance)
            elif action == 4:
                break
            else:
                print("Invalid Action")

balance_amount = 1500000
person1 = CustomException(balance_amount)
person1.atm_simulation()
