
class Bank_Account:
    def __init__(self, Account_Number, Balance):
        self.deposit = None
        self.withdraw = None
        self.Account_Number = Account_Number
        self.Bank_Balance = Balance

    # DEPOSIT CODE--------------------
    def deposit_money(self):
        self.deposit = int(input("Enter the amount to be deposit:"))
        self.Bank_Balance += self.deposit
        print(f"Your Account (AC_No: {self.Account_Number}) credited by RS.{self.deposit}/ ")

        # Balance checker-----------
        display_balance = int(input("Press 1 to display balance Press 2 if not needed:"))
        if display_balance == 1:
            print(f"Current Bank Balance =  RS.{self.Bank_Balance}/")
            print("Thank you, your transaction successfully completed,Share your feed back")
        else:
            print("Thank you, your transaction successfully completed,Share your feed back")

    # WITHDRAWAL CODE-------------------
    def withdraw_money(self):
        self.withdraw = int(input("Enter the amount to be withdraw:"))

        # When the withdrawal amount is less than balance-------------------
        if self.withdraw <= self.Bank_Balance:
            self.Bank_Balance -= self.withdraw
            print(f"Your Account (AC_No: {self.Account_Number}) debited by RS.{self.withdraw}/ ")
            # Balance checker-----------
            display_balance = int(input("Press 1 to display balance Press 2 if not needed:"))
            if display_balance == 1:
                print(f"Current Bank Balance =  RS.{self.Bank_Balance}/")
                print("Thank you, your transaction successfully completed,Share your feed back")
            else:
                print("Thank you, your transaction successfully completed,Share your feed back")

        # When the withdrawal amount is greater than balance------------
        elif self.withdraw > self.Bank_Balance:
            print(f"Insufficient balance, Kindly check your bank balance")
            # Checking balance
            display_balance = int(input("Press 1 to display balance Press 2 to cancel your transaction:"))
            if display_balance == 1:
                print(f"Current Bank Balance =  RS.{self.Bank_Balance}/")
            else:
                print("Sorry, your transaction failed,Please try again")
            continue_transaction = int(input("Press 5 if you want to continue transaction or Press 6 to cancel "
                                             "transaction:"))
            if display_balance == 1 and continue_transaction == 5:
                self.withdraw = int(input("Enter the amount to be withdraw:"))
                # When the withdrawal amount is less than balance
                if self.withdraw <= self.Bank_Balance:
                    self.Bank_Balance -= self.withdraw
                    print(f"Your Account (AC_No: {self.Account_Number}) debited by RS.{self.withdraw}/ ")
                    # Balance checker-----------
                    display_balance = int(input("Press 1 to display balance Press 2 if not needed:"))
                    if display_balance == 1:
                        print(f"Current Bank Balance =  RS.{self.Bank_Balance}/")
                        print("Thank you, your transaction successfully completed,Share your feed back")
                    else:
                        print("Thank you, your transaction successfully completed,Share your feed back")
            elif continue_transaction == 6:
                print("Sorry, your transaction failed,Please try again")

def input_fun():
    input_acc_No = int(input("Enter the account number:"))

    input_balance = 200000

    input_debit_or_credit = int(input("Press 1 for deposit Press 2 for withdrawal:"))

    transaction_1 = Bank_Account(input_acc_No, input_balance)

    if input_debit_or_credit == 1:
        transaction_1.deposit_money()
        pass
    elif input_debit_or_credit == 2:
        transaction_1.withdraw_money()
input_fun()





