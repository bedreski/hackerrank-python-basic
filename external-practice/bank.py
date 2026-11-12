
class BankAccount():

    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return self.balance

    def get_balance(self):
        return self.balance

#Main
#B - initial account balance
b = int(input())
if 0 <= b <= 10**9:
    account = BankAccount(b)
else:
    print('Balance is out of range.')

#N - number of operations
n = int(input())

# The next N lines contain an operation and an integer amount, separated by space
if 0 <= n <= 100:
    for i in range(n):
        try:
            operation, amount = input().split()
            amount = int(amount)

        except ValueError:
            print("Invalid input.")

        if operation == 'DEPOSIT':
            account.deposit(amount)
            print(account.get_balance())
        elif operation == 'WITHDRAW':
            account.withdraw(amount)
            print(account.get_balance())
        elif operation == 'BALANCE':
            print(account.get_balance())

# The operations are:
# DEPOSIT X: deposits amount x
# WITHDRAW X: withdraws amount x
# BALANCE 0: requests the current account balance. The second argument is always zero for this operation
    
