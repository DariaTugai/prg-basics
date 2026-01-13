class Bank_account():
    def __init__(self, number, balance):
        self.number= number
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance-=amount
       

    def get_data(self):
        print(f'Bank Account No: {self.number}')             
        print(f'Balance: PLN {self.balance}')

acc=Bank_account('12 3456 5555 9090 1111 0000 7722',0)
acc.deposit(25.30)
acc.get_data()
acc.withdraw(26)
acc.get_data()