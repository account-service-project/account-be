from domain.db_connect import db
from domain.account.models import Account


class AccountRepository:
    @staticmethod
    def save(account: Account):
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def get_by_account_number(account_number: str):
        return db.session.query(Account).filter(Account.account_number == account_number).first()

    @staticmethod
    def get_count_account(member_id: int) -> int:
        return db.session.query(Account).filter(Account.member_id == member_id).count()
