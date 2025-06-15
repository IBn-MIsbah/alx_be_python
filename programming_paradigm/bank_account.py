class BankAccount:
    def __init__(self, account_balance ):
        self.account_balance = account_balance 

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
        
    def withdraw(self, amount):
        if 0 < amount and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance # "Private" attribute by convention

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited {amount}. New balance: {self.__balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.__balance}")
#         else:
#             print("Invalid withdrawal amount or insufficient funds.")

#     def get_balance(self):
#         return self.__balance

# account = BankAccount(1000)
# account.deposit(500)
# # print(account.__balance) # This would raise an AttributeError because of name mangling
# print(account.get_balance()) # Output: 1500