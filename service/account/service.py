import random
from flask_smorest import abort
from domain.account.repository import AccountRepository
from domain.account.models import Account
from config.constants import ACCOUNT_LIMIT, EXCESS_ERROR_MESSAGES


class AccountService:
    def __init__(self):
        self.repository = AccountRepository()

    def is_duplicated(self, number: str) -> bool:
        duplicate_number = self.repository.get_by_account_number(account_number=number)
        return True if duplicate_number else False

    def count_account(self, member_id: int) -> int:
        count = self.repository.get_count_account(member_id=member_id)
        return count

    def create_random_13_digit(self) -> int:
        return random.randint(1111111111111, 9999999999999)

    def create_account_number(self) -> str:
        account_number = str(self.create_random_13_digit())
        while self.is_duplicated(account_number):
            account_number = self.create_random_13_digit()
        return str(account_number)

    def create_account(self, member_id: int):
        if self.count_account(member_id=member_id) >= ACCOUNT_LIMIT:
            abort(400, message=EXCESS_ERROR_MESSAGES)
        else:
            account_number = self.create_account_number()
            account = Account(account_number=account_number, member_id=member_id)
            return self.repository.save(account)
