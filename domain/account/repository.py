from domain.db_connect import db
from domain.account.models import Account
from flask import jsonify
from typing import List

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
    
    @staticmethod
    def get_all_accounts(member_id: int):
        return Account.query.filter(Account.member_id == member_id).all()

    @staticmethod
    def delete_account(member_id:int, account_id: int):
        delete_to_account = Account.query.filter(Account.member_id == member_id, Account.id == account_id).first_or_404()
        db.session.delete(delete_to_account)
        db.session.commit()
        return {"success": True, "message":"계좌가 삭제되었습니다."}
