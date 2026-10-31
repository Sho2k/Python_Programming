class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(5000)
print("Balance:", account.get_balance())
