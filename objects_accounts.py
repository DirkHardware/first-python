import datetime
import pytz


class Account:
    """ Simple account class with balance"""

    # The blow is a static method. A static method is shares by alll instances
    # of the class and is used for classes that don't need self
    # and aren't part of normal operations.

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []

        print("Account created for" + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        # note the chaining of conditionals here
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The account must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    anderson = Account("Anderson", 0)
    anderson.show_balance()

    anderson.deposit(1000)
    anderson.withdraw(500)

    anderson.withdraw(2000)
    anderson.show_transactions()