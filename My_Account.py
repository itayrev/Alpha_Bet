from Bank_Account import BankAccount
from Linked_List import LinkedList
from Linked_List import Node
from Processor import Processor
from datetime import date

NUM_OF_PAYMENTS = 12
PAYMENT_PERIOD = 7
weeks_counter = False


def init_linked_list():
    linked_list = LinkedList()
    for i in range(1, NUM_OF_PAYMENTS + 1):
        linked_list.add_node(Node(i))
    return linked_list


def check_amount(amount):
    if not amount.isdigit() or float(amount) < 0:
        raise TypeError((
            'Invalid parameter type(s) - '
            'amount={0} must be positive Decimal'.format(type(amount))))


class MyAccount:

    def __init__(self):
        self.my_account = BankAccount()
        self.my_processor = Processor()
        self.last_payment_dairy = dict()

    def perform_advance(self, dst_bank_account, amount):
        try:
            check_amount(amount)
            amount = float(amount)
            partial_amount = amount / NUM_OF_PAYMENTS
            my_payments = init_linked_list()
            self.last_payment_dairy[dst_bank_account] = date.today()
            while not my_payments.is_empty():
                cur_transaction = self.my_processor.perform_transaction(self.my_account, dst_bank_account,
                                                                        partial_amount,
                                                                        "credit")
                report = self.my_processor.download_report()
                if report[cur_transaction] == "fail":
                    my_payments.add_node(Node(my_payments.head.data))
                my_payments.remove_head()
                self.last_payment_dairy[dst_bank_account] = date.today()
                yield
        except TypeError:
            print("please enter positive number as your amount\n")


if __name__ == '__main__':
    my = MyAccount()
    b1 = BankAccount()
    b2 = BankAccount()
    gen = my.perform_advance(b1, '120')
    gen2 = my.perform_advance(b2, '30')
    dst_accounts = [b1, b2]
    accounts_generator = {b1: gen, b2: gen2}
    while dst_accounts:
        for account in dst_accounts:
            try:
                if account not in my.last_payment_dairy or abs(
                        date.today() - my.last_payment_dairy[account]).days < PAYMENT_PERIOD:
                    next(accounts_generator[account])
            except StopIteration:
                dst_accounts.remove(account)
                continue
