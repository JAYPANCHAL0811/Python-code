class BankAccount:
    def __init__(self, person_name, account_balance):
        self.person_name = person_name
        self.account_balance = account_balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.account_balance = self.account_balance + deposit_amount
            print("Deposit successful.")
        else:
            print("Enter a positive amount.")

    def display(self):
        print("Account holder:", self.person_name)
        print("Balance:", self.account_balance)

bank_obj = BankAccount("Meera Patel", 15000)
bank_obj.deposit(2500)
bank_obj.display()
