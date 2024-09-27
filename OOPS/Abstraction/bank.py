

# accno.,bnkname,balance,actype

class bank():

    def create_account(self,acc_no,acc_type):

        self.acc_no=acc_no
        self.bank_name="Canara"
        self.__balance=1500
        self.acc_type=acc_type

    def deposit(self,deposit_amount):
        self.__balance=self.__balance+deposit_amount
        print(f"Your {self.bank_name} with Account_no. {self.acc_no} has been credited with {deposit_amount}.\nCurrent balance :-{self.__balance}")

    def withdraw(self,withdraw_amount):
        if self.__balance>=withdraw_amount:
            self.__balance=self.__balance-withdraw_amount
            print(f"Your {self.bank_name} A/C {self.acc_no} debited for {withdraw_amount}.\nCurrent balance :-{self.__balance}")

        else:
            print("Insufficient balance")


    def get_balance(self):
        print(self.__balance)


account_1=bank()

account_1.create_account(6725839177,"Savings")

# account_1.withdraw(2000)

account_1.deposit(2500)

account_1.withdraw(2550)
print(account_1.__balance)