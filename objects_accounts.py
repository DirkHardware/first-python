import datetime
import pytz


class Account:
    """ Simple account class with balance"""

    # The blow is a static method. A static method is shares by all instances
    # of the class and is used for classes that don't need self
    # and aren't part of normal operations.

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        # Attributes starting with an underscore are for INTERNAL USE ONLY
        self._name = name
        # Attributes starting with two underscores are "mangled" by Python,
        # i.e. under the hood their name actually begins with the class they belong to
        # so they cannot be changed from outside, like I am trying to do on line 67
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]

        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        # note the chaining of conditionals here
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The account must be greater than zero and no more than your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
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

    julia = Account("Julia", 800)
    julia.__balance = 200
    julia.deposit(100)
    julia.withdraw(200)
    julia.show_transactions()
    julia.show_balance()
    # If we really wanted to change the mangled balance for Julia's account
    # we would do this:
    # julia.Account__balance = 200
