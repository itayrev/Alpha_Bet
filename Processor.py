import string
from datetime import date
import random


class Processor:
    def __init__(self):
        self.__transactions = dict()

    def perform_transaction(self, src_bank_account, dst_bank_account, amount, direction):
        trans_num = ''.join(random.choice(string.digits) for x in range(6))
        if direction == "credit":
            result_flag = src_bank_account.debit(amount)
            if result_flag:
                dst_bank_account.credit(amount)
        else:
            result_flag = dst_bank_account.debit(amount)
            if result_flag:
                src_bank_account.credit(amount)
        if result_flag:
            self.__transactions[trans_num] = "success"
        else:
            self.__transactions[trans_num] = "fail"
        return trans_num

    def download_report(self):
        return self.__transactions
