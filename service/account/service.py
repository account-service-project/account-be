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

    def get_accounts_list(self, member_id: int):
        if self.count_account(member_id=member_id) > 0:
            accounts = self.repository.get_all_accounts(member_id=member_id)
            account_list = []
            for account in accounts:
                account_dict = {
                    'id':account.id,
                    'account_number':account.account_number,
                    'current_balance':account.current_balance,
                    'member_id':account.member_id,
                    'created_data':account.created_date
                }
                account_list.append(account_dict)
            return account_list
        else : 
            abort(400, "해당유저는 계좌가 존재하지 않습니다.")
        
    def delete_account(self, member_id: int, account_id: int):
        return self.repository.delete_account(member_id=member_id, account_id=account_id)