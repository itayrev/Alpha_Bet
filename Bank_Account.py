import random
import string


class BankAccount:
    def __init__(self):
        self.__account_id = ''.join(random.choice(string.digits) for x in range(6))
        self.__balance = 0

    def credit(self, amount):
        self.__balance += amount

    def debit(self, amount):
        if self.__balance - amount < 0:
            return False
        self.__balance -= amount
        return True

    def __str__(self):
        return "Account_ID: " + str(self.__account_id) + " Balance: " + str(self.__balance)
