class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self._balance = balance
        self.__account_number = account_number
    
    def deposit(self, amount):  
        self._balance += amount

    def withdraw(self, amount): 
        if amount > self._balance: 
            raise ValueError("You don't have so much money!!!")
        self._balance -= amount

    def get_balance(self): 
        return self._balance

    def display_info(self): 
        print(f"Name: {self.name}")
        print(f"Balance: {self._balance}")
        print(f"Account number: {self.__account_number}")

class SavingAccount(BankAccount): 
    def __init__(self, name, balance, account_number, interest_rate):
        super().__init__(name, balance, account_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate

# Example:    
user1 = SavingAccount(name="Ramil", balance=150, account_number=123, interest_rate=0.05)

print(user1.get_balance())
user1.apply_interest()
print(user1.get_balance())

