# Add these methods to class Account - deposit, withdraw. Create two instances of account and verify they work as expected.
class Account:
    def __init__(self,bank_name,acc_bal,amount,acc_name,acc_number):
        self.bank_name=bank_name
        self.amount=amount
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.acc_bal=acc_bal
       

    def deposit(self):
        return f"{self.bank_name} confirmed that {self.acc_name} and account number {self.acc_number}has deposited {self.amount}.Your balance was {self.acc_bal} and your new balance is now {self.acc_bal+self.amount}"

    def withdraw(self):
        return f"{self.bank_name} confirmed that {self.acc_name} with account number {self.acc_number} has withdrawn {self.amount}. Your balance was {self.acc_bal} and your new balance is now {self.acc_bal-self.amount}"
      
