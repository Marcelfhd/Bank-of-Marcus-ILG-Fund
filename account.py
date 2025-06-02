from abc import ABC, abstractmethod
import bank
import utils
import time


class Account:

    num_of_accounts = 0

    def __init__(self, owner: str, balance: float, account_number: str) -> None:
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        self.transaction_history_list = []
        Account.num_of_accounts += 1

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"You have successfully deposited ${amount:.2f} into your account.")
        self.store_in_transaction_history("Deposit", amount)


    def receive_transfer(self, amount: float) -> None:
        self.balance += amount
        self.store_in_transaction_history("R_Transfer", amount)

    def transfer_money(self) -> None:

        while True:

            print("--------q to quit--------")

            transfer_target_name: str = input("Please enter the name of the account" +
                                              " you would like to transfer funds to: ").lower()
            if transfer_target_name.lower() == "q":
                break
            if not utils.bad_name_catcher(transfer_target_name):
                print("Name must be at least three characters long and contain only alphabetic characters. No spaces.")
                continue

            transfer_target_number: str = input("Please enter the account number of the" +
                                                " account you would like to transfer funds to: ")
            if transfer_target_number.lower() == "q":
                break
            if not utils.bad_account_number_catcher(transfer_target_number):
                print("Invalid account number.")
                continue

            transfer_account_type = bank.transfer_account_check(transfer_target_name, transfer_target_number)

            if transfer_account_type == "404":
                print("ERROR: Account not found!")
                continue

            key = (transfer_target_name, transfer_target_number, transfer_account_type)
            transfer_target = bank.bank_users[key]

            while True:
                transfer_amount = input("How much would you like to transfer? ")

                if transfer_amount.lower() == "q":
                    return
                if not utils.bad_number_catcher(transfer_amount):
                    continue

                transfer_amount = float(transfer_amount)

                if not self.withdraw(transfer_amount):
                    continue

                transfer_target.receive_transfer(transfer_amount)
                print(f"You have successfully transferred funds to:")
                print(f"Name: {transfer_target_name.capitalize()}")
                print(f"Number: {transfer_target_number}")
                self.store_in_transaction_history("S_Transfer", transfer_amount)
                return


    def store_in_transaction_history(self, transaction_type: str, transaction_amount: float) -> None:
        transaction_time = utils.get_current_time()
        updated_balance = self.balance
        self.transaction_history_list.append({"time": transaction_time,
                                              "type": transaction_type,
                                              "amount": transaction_amount,
                                              "balance": updated_balance
                                              })

    def transaction_history(self):

        if not self.transaction_history_list:
            print("-" * 60)
            print("This account has no recorded transactions")
            print("-" * 60)

        else:
            print()
            print(f"{'Time':<10} | {'Transaction Type':<18} | {'Amount':<10} | {'New Balance'}")
            print("-" * 60)
            for txn in self.transaction_history_list:
                print(f"{txn['time']:<10} | {txn['type']:<18} | ${txn['amount']:<9.2f} | ${txn['balance']:.2f}")
            print("-" * 60)
            print()
            time.sleep(4)


    @abstractmethod
    def check_balance(self) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class CheckingAccount(Account):     # allows overdraft up to 100$, limited withdrawal amount (say 1000 at a time)

    def __init__(self, owner, balance, account_number):
        super().__init__(owner, balance, account_number)
        self.withdraw_limit = 1000
        self.withdraw_counter = 0

    def check_balance(self) -> None:
        print(f"Your current balance is ${self.balance:.2f}")

    def reset_withdraw_counter(self):
        self.withdraw_counter = 0

    def withdraw(self, amount: float) -> bool:

        if self.withdraw_counter + amount > self.withdraw_limit:
            print("This transaction will exceed your withdrawal limit of $1000.")
            print(f"You have already withdrawn ${self.withdraw_counter} this session.")
            return False

        if self.balance < 0:
            print("You must return your account to good standing before you may overdraft again.")
            return False

        if self.balance - amount < -100:
            print("Insufficient funds.")
            return False

        if self.balance - amount < 0:
            while True:
                confirmation = input("This withdrawal will overdraft. Continue? (Y/N): ")
                if confirmation.lower() == "n":
                    return False
                if confirmation.lower() == "y":
                    self.balance -= amount
                    self.withdraw_counter += amount
                    self.store_in_transaction_history("Withdraw_overdraft", amount)
                    print(f"You have successfully withdrawn ${amount}")
                    return True
                else:
                    print("Invalid input.")

        self.balance -= amount
        self.withdraw_counter += amount
        print(f"You have successfully withdrawn ${amount}")
        self.store_in_transaction_history("Withdraw", amount)
        return True


class SavingsAccount(Account):        # has earn interest function, limited # of withdrawals, and fees? if you go over?
    def __init__(self, owner, balance, account_number):
        super().__init__(owner, balance, account_number)
        self.number_of_withdrawals = 0
        self.withdraw_limit = 3
        self.fee = 100
        self.interest_counter = 0
        self.interest_counter_cap = 2
        self.interest_rate = 0.05

    def reset_number_of_withdrawals(self) -> None:
        self.number_of_withdrawals = 0

    def reset_interest_counter_cap(self) -> None:
        self.interest_counter = 0

    def check_balance(self) -> None:
        print(f"Your current balance is ${self.balance:.2f}")

    def earn_interest(self) -> None:
        if self.interest_counter < self.interest_counter_cap:
            self.store_in_transaction_history("Interest", self.balance * self.interest_rate)
            self.balance += self.balance * self.interest_rate
            self.interest_counter += 1
            print(f"Interest rate of {self.interest_rate * 100}% has been applied to your balance!")
            print(f"Your new balance is ${self.balance:.2f}")
        else:
            print("You have exceeded the maximum amount of times you may apply interest this session.")


    def withdraw(self, amount: float) -> bool:  # allows one free withdrawal per login after wards charges fee each time
                                                                                        # caps at 3 withdraws per session
        if self.number_of_withdrawals > self.withdraw_limit:
            print("You have exceeded the number of times you may withdraw.")
            return False

        if amount > self.balance:
            print(f"Insufficient funds. Your balance is ${self.balance:.2f} and",
            f"you are attempting to withdraw ${amount}.")
            return False

        if self.number_of_withdrawals > 0:
            if self.balance - (amount + self.fee) < 0:
                print(f"Insufficient funds. This withdrawal will also incur a fee of ${self.fee},",
                "which exceeds your balance.")
                return False
            print(f"Warning! This transaction will incur a withdrawal fee of ${self.fee}.")
            confirmation = input("Continue? (Y/N): ")
            if confirmation.lower() == "n":
                return False
            if confirmation.lower() == "y":
                self.balance -= amount
                self.store_in_transaction_history("Withdraw", amount)
                self.balance -= self.fee
                self.store_in_transaction_history("Withdraw_fee", self.fee)
                self.number_of_withdrawals += 1
                print(f"You have successfully withdrawn ${amount}")
                print(f"For exceeding your daily free withdrawal",
                f"you have also been charged ${self.fee}")
                return True
            else:
                print("Invalid input.")

        self.balance -= amount
        self.number_of_withdrawals += 1
        self.store_in_transaction_history("Withdraw", amount)
        print(f"You have successfully withdrawn ${amount}")
        return True


class BusinessAccount(Account):   # allows higher withdrawal amounts (say 5000), but has fees under some condition?
    def __init__(self, owner, balance, account_number):
        super().__init__(owner, balance, account_number)
        self.withdraw_limit = 5000
        self.withdraw_counter = 0

    def check_balance(self) -> None:
        print(f"Your current balance is ${self.balance:.2f}")

    def reset_withdraw_counter(self):
        self.withdraw_counter = 0

    def withdraw(self, amount: float) -> bool:

        if self.withdraw_counter + amount > self.withdraw_limit:
            print("This transaction will exceed your withdrawal limit of $5000.")
            print(f"You have already withdrawn ${self.withdraw_counter} this session.")
            return False

        if amount > self.balance:
            print(f"Insufficient funds. Your balance is ${self.balance:.2f} and",
                  f"you are attempting to withdraw ${amount}.")
            return False

        self.balance -= amount
        self.withdraw_counter += amount
        self.store_in_transaction_history("Withdraw", amount)
        print(f"You have successfully withdrawn ${amount}")
        return True


    def do_business(self):
        print("Initializing...")
        time.sleep(2)

        print(utils.business_top_g())
        time.sleep(3)

        print("Scheduling meetings..")
        time.sleep(2)
        print("Shaking hands..")
        time.sleep(2)

        print(utils.business_top_g())
        time.sleep(3)
        print("Doing business.")
        time.sleep(2)
        print("Business has been done.")
        time.sleep(2)

        print("-" * 40)
        print(utils.alpha_male_top_g())
        print("-" * 40)
        time.sleep(2)

        self.balance += 10_000
        self.store_in_transaction_history("Business", 10_000)


