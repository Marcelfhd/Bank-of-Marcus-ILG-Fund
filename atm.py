import time
import bank
import utils


def atm():
    while True:

        print("Welcome to Bank")
        print("1: Login")
        print("2: Create Account")
        print("3: Help")
        print("4: Exit")
        user_request = input("Please indicate what you would like to do: ")

        if user_request == "1":
            print("1: Checking Account")
            print("2: Savings Account")
            print("3: Business Account")
            sub_request = input("Which account would you like to log into? ")

            if sub_request == "1":
                print("----q to quit-----")

                while True:
                    username = input("Please enter your name: ").lower()
                    if username == "q":
                        break
                    if not utils.bad_name_catcher(username):
                        print("Name must be at least three characters long and",
                              "contain only alphabetic characters. No spaces.")
                        continue

                    account_number = input("Please enter your account number: ")
                    if account_number.lower() == "q":
                        break
                    if not utils.bad_account_number_catcher(account_number):
                        print("Invalid account number.")
                        continue

                    account_type = "checking"
                    account_request = "checking"
                    if bank.check_account_exists(username, account_number, account_type, account_request):
                        bank.logged_into_checking(username, account_number, account_type)
                        break
                    else:
                        break


            elif sub_request == "2":
                print("----q to quit-----")

                while True:
                    username = input("Please enter your name: ").lower()
                    if username == "q":
                        break
                    if not utils.bad_name_catcher(username):
                        print("Name must be at least three characters long and",
                              "contain only alphabetic characters. No spaces.")
                        continue

                    account_number = input("Please enter your account number: ")
                    if account_number.lower() == "q":
                        break
                    if not utils.bad_account_number_catcher(account_number):
                        print("Invalid account number.")
                        continue

                    account_type = "savings"
                    account_request = "savings"
                    if bank.check_account_exists(username, account_number, account_type, account_request):
                        bank.logged_into_savings(username, account_number, account_type)
                        break
                    else:
                        break

            elif sub_request == "3":
                print("----q to quit-----")

                while True:
                    username = input("Please enter your name: ").lower()
                    if username == "q":
                        break
                    if not utils.bad_name_catcher(username):
                        print("Name must be at least three characters long and",
                              "contain only alphabetic characters. No spaces.")
                        continue

                    account_number = input("Please enter your account number: ")
                    if account_number.lower() == "q":
                        break
                    if not utils.bad_account_number_catcher(account_number):
                        print("Invalid account number.")
                        continue

                    account_type = "business"
                    account_request = "business"
                    if bank.check_account_exists(username, account_number, account_type, account_request):
                        bank.logged_into_business(username, account_number, account_type)
                        break
                    else:
                        break

            else:
                print("Invalid input")


        elif user_request == "2":
            bank.create_account()


        elif user_request == "3":
            while True:
                print("---- q to quit ----")
                print("1: Checking Account")
                print("2: Savings Account")
                print("3: Business Account")
                sub_request = input("Which account would you like help with?: ")

                if sub_request.lower() == "q":
                    break

                if sub_request == "1":
                    print()
                    print("----CHECKING ACCOUNT----")
                    print("- Allows overdrafting, up to $100.")
                    print("- When overdrafted, you may not overdraft again until you return",
                          "your account to good standing (Balance must be at least 0).")
                    print("- Can not earn interest.")
                    print("- May withdraw / outgoing transfer as many times as you like, up to a",
                          "total limit of $1000 per log in session.")
                    print()
                    time.sleep(5)
                    continue

                if sub_request == "2":
                    print()
                    print("----SAVINGS ACCOUNT----")
                    print("- Can not overdraft.")
                    print("- Has the ability to earn interest (current rate of 5%).",
                          "You may earn interest twice per log in session.")
                    print("- The number of withdrawals / outgoing transfers are limited,",
                          "but there is no monetary limit per transaction.")
                    print("- You are allowed one free withdrawal / outgoing transfer per log in session.")
                    print("- Afterwards, you will incur a fee for each additional withdrawal/transfer,",
                    "up to a total cap of 3 per log in session.")
                    print()
                    time.sleep(5)
                    continue

                if sub_request == "3":
                    print()
                    print("----BUSINESS ACCOUNT----")
                    print("- Can not overdraft.")
                    print("- Can not earn interest.")
                    print("- No limit on the number of withdrawals / outgoing transfers, but there is a",
                    "total monetary limit of $5000 per log in session.")
                    print("- Has the special ability to 'Do Business'")
                    print()
                    time.sleep(5)
                    continue

                else:
                    print("Invalid input")
                    continue

        elif user_request == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid input.")



if __name__ == "__main__":
    atm()
