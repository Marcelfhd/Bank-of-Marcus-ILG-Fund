import time
import random
import utils
from account import CheckingAccount
from account import SavingsAccount
from account import BusinessAccount

bank_users = {}


def create_account():
   print("1: Checking Account")
   print("2: Savings Account")
   print("3: Business Account")
   print("---- q to quit ----")
   request = input("Which account would you like to create?: ")

   if request == "1":
       create_checking()
       time.sleep(2)

   elif request == "2":
       create_savings()
       time.sleep(2)

   elif request == "3":
       create_business()
       time.sleep(2)

   elif request.lower() == "q":
       pass

   else:
       print("Invalid input")


def create_checking():
    print("You are creating a CHECKING account!")
    print("----q to quit-----")

    while True:
        username = input("Please enter your name: ").lower()
        if username == "q":
            break
        if not utils.bad_name_catcher(username):
            print("Name must be at least three characters long and contain only alphabetic characters. No spaces.")
            continue

        print(f"The name associated with your bank account is: {username.capitalize()}")
        confirmation = input("Is this correct? (Y/N): ").lower()
        if confirmation != "y":
            continue

        while True:
            deposit = input("How much would you like to deposit into your CHECKING account?: ")
            if deposit == "q":
                return
            if not utils.bad_number_catcher(deposit):
                continue

            deposit = float(deposit)
            account_type = "checking"
            random_account_number = utils.account_number_creator()
            new_checking_account = CheckingAccount(owner=username, balance=deposit,
                                                   account_number=random_account_number)
            bank_users[(username, random_account_number, account_type)] = new_checking_account
            print("-" * 60)
            print("Success! Checking account created!")
            print(f"Your username is {username.capitalize()} and your account number is {random_account_number}")
            print("-" * 60)
            return


def create_savings():
    print("You are creating a SAVINGS account!")
    print("----q to quit-----")

    while True:
        username = input("Please enter your name: ").lower()
        if username == "q":
            break
        if not utils.bad_name_catcher(username):
            print("Name must be at least three characters long and contain only alphabetic characters. No spaces.")
            continue

        print(f"The name associated with your bank account is: {username.capitalize()}")
        confirmation = input("Is this correct? (Y/N): ").lower()
        if confirmation != "y":
            continue

        while True:
            deposit = input("How much would you like to deposit into your SAVINGS account?: ")
            if deposit == "q":
                return
            if not utils.bad_number_catcher(deposit):
                continue

            deposit = float(deposit)
            account_type = "savings"
            random_account_number = utils.account_number_creator()
            new_savings_account = SavingsAccount(owner=username, balance=deposit,
                                                   account_number=random_account_number)
            bank_users[(username, random_account_number, account_type)] = new_savings_account
            print("-" * 60)
            print("Success! Savings account created!")
            print(f"Your username is {username.capitalize()} and your account number is {random_account_number}")
            print("-" * 60)
            return



def create_business():
    print("You are creating a BUSINESS account!")
    print("----q to quit-----")

    while True:
        username = input("Please enter your name: ").lower()
        if username == "q":
            break
        if not utils.bad_name_catcher(username):
            print("Name must be at least three characters long and contain only alphabetic characters. No spaces.")
            continue

        print(f"The name associated with your bank account is: {username.capitalize()}")
        confirmation = input("Is this correct? (Y/N): ").lower()
        if confirmation != "y":
            continue

        while True:
            deposit = input("How much would you like to deposit into your BUSINESS account?: ")
            if deposit == "q":
                return
            if not utils.bad_number_catcher(deposit):
                continue

            deposit = float(deposit)
            account_type = "business"
            random_account_number = utils.account_number_creator()
            new_business_account = BusinessAccount(owner=username, balance=deposit,
                                                   account_number=random_account_number)
            bank_users[(username, random_account_number, account_type)] = new_business_account
            print("-" * 60)
            print("Success! Business account created!")
            print(f"Your username is {username.capitalize()} and your account number is {random_account_number}")
            print("-" * 60)
            return


def check_account_type(username: str, account_number: str, account_request: str) -> bool:
    for key in bank_users:
        if key[0] == username and key[1] == account_number:
            account_type = key[2]
            if account_type == account_request:
                return True
            else:
                print("-----------------------------------------------------------")
                print(f"ERROR: You have requested to log into a {account_request} account with a {account_type} account.")
                print("-----------------------------------------------------------")
                return False
    else:
        print("-----------------------------------------------------------")
        print("ERROR: Username or account number is incorrect / not found!")
        print("-----------------------------------------------------------")
        return False


def check_account_exists(username: str, account_number: str, account_type: str, account_request: str) -> bool:

    if not check_account_type(username, account_number, account_request):
        return False

    if not (username, account_number, account_type) in bank_users:
        print("How did you get here?")
        return False

    print("You have successfully logged in!")
    return True


def transfer_account_check(transfer_target_name: str, transfer_target_number: str) -> str:

    for key in bank_users:
        if key[0] == transfer_target_name and key[1] == transfer_target_number:
            transfer_target_account_type = key[2]
            return transfer_target_account_type
    else:
        return "404"



def logged_into_checking(username: str, account_number: str, account_type: str) -> None:

    key = (username, account_number, account_type)
    checking_account = bank_users[key]

    print("---------------------")
    print(f"Welcome {username.capitalize()}!")
    print("---------------------")
    print()
    time.sleep(1)

    while True:
        print("1: Check Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Transfer funds")
        print("5: View Transaction History")
        print("6: Log out")
        request = input("Select an option: ")

        if request == "1":

            checking_account.check_balance()
            time.sleep(1)
            print()

        elif request == "2":

            while True:
                deposit = input("Please enter amount to deposit (q to quit): ")
                if deposit.lower() == "q":
                    break

                if not utils.bad_number_catcher(deposit):
                    continue

                deposit = float(deposit)
                checking_account.deposit(deposit)
                checking_account.check_balance()


        elif request == "3":

            while True:
                withdraw_amount = input("Please enter amount to withdraw (q to quit): ")
                if withdraw_amount.lower() == "q":
                    break
                if not utils.bad_number_catcher(withdraw_amount):
                    continue

                withdraw_amount = float(withdraw_amount)

                if not checking_account.withdraw(withdraw_amount):
                    print("Withdrawal failed")

                else:
                    checking_account.check_balance()
                    time.sleep(2)
                    break


        elif request == "4":
            checking_account.transfer_money()

        elif request == "5":
            checking_account.transaction_history()

        elif request == "6":
            checking_account.reset_withdraw_counter()
            print("Logging out")
            break
        else:
            print("Invalid input")


def logged_into_savings(username, account_number, account_type):

    key = (username, account_number, account_type)
    savings_account = bank_users[key]

    print("---------------------")
    print(f"Welcome {username.capitalize()}!")
    print("---------------------")
    print()
    time.sleep(1)

    while True:
        print("1: Check Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Transfer funds")
        print("5: Earn Interest")
        print("6: View Transaction History")
        print("7: Log out")
        request = input("Select an option: ")

        if request == "1":
            savings_account.check_balance()
            time.sleep(1)
            print()

        elif request == "2":

            while True:
                deposit = input("Please enter amount to deposit (q to quit): ")
                if deposit.lower() == "q":
                    break
                if not utils.bad_number_catcher(deposit):
                    continue

                deposit = float(deposit)
                savings_account.deposit(deposit)
                savings_account.check_balance()
                break


        elif request == "3":

            while True:
                withdraw_amount = input("Please enter amount to withdraw (q to quit): ")
                if withdraw_amount.lower() == "q":
                    break
                if not utils.bad_number_catcher(withdraw_amount):
                    continue

                withdraw_amount = float(withdraw_amount)

                if not savings_account.withdraw(withdraw_amount):
                    print("Withdrawal failed")

                else:
                    savings_account.check_balance()
                    time.sleep(2)
                    break


        elif request == "4":
            savings_account.transfer_money()

        elif request == "5":
            savings_account.earn_interest()
            time.sleep(1)

        elif request == "6":
            savings_account.transaction_history()

        elif request == "7":
            savings_account.reset_number_of_withdrawals()
            savings_account.reset_interest_counter_cap()
            print("Logging out")
            break

        else:
            print("Invalid input")


def logged_into_business(username: str, account_number: str, account_type: str) -> None:

    key = (username, account_number, account_type)
    business_account = bank_users[key]

    print("---------------------")
    print(f"Welcome {username.capitalize()}!")
    print("---------------------")
    print()
    time.sleep(1)

    while True:
        print("1: Check Balance")
        print("2: Deposit")
        print("3: Withdraw")
        print("4: Do Business")
        print("5: Transfer funds")
        print("6: View Transaction History")
        print("7: Log out")
        request = input("Select an option: ")

        if request == "1":
            business_account.check_balance()
            time.sleep(1)
            print()

        elif request == "2":

            while True:
                deposit = input("Please enter amount to deposit (q to quit): ")
                if deposit.lower() == "q":
                    break
                if not utils.bad_number_catcher(deposit):
                    continue

                deposit = float(deposit)
                business_account.deposit(deposit)
                business_account.check_balance()
                break

        elif request == "3":

            while True:
                withdraw_amount = input("Please enter amount to withdraw (q to quit): ")
                if withdraw_amount.lower() == "q":
                    break
                if not utils.bad_number_catcher(withdraw_amount):
                    continue

                withdraw_amount = float(withdraw_amount)

                if not business_account.withdraw(withdraw_amount):
                    print("Withdrawal failed")

                else:
                    business_account.check_balance()
                    time.sleep(2)
                    break

        elif request == "4":
            business_account.do_business()

        elif request == "5":
            business_account.transfer_money()

        elif request == "6":
            business_account.transaction_history()

        elif request == "7":
            business_account.reset_withdraw_counter()
            print("Logging out")
            break

        else:
            print("Invalid input")





if __name__ == "__main__":
    pass







