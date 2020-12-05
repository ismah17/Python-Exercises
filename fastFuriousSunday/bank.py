import datetime
import pytz


class Account:
    """A simple class to deposit, withdraw and show balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []

    def deposit(self, amount):
        self.balance += amount
        self.amount = amount
        self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.amount = amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("balance is not enough to withdraw that amount, your balance is {}".format(self.balance))

    def print_balance(self):
        print("your balance is ", self.balance)

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                trans_type = "deposited"
            else:
                trans_type = "withdrawn"
                amount *= -1
            print("{:6} {} from total balance of {} on {} (local time was {})".format(amount, trans_type, self.balance, date, date.astimezone()))



if __name__ == '__main__':
    ishani = Account("Ishani", 0)
    ishani.print_balance()

    ishani.deposit(1000)
    ishani.print_balance()
    ishani.withdraw(100)
    ishani.print_balance()
    ishani.show_transactions()
    print(ishani.transaction_list)
