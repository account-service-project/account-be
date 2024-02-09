from domain.db_connect import db
from domain.transaction.models import UseBalanceHistory


class UseBalanceHistoryRepository:
    @staticmethod
    def save(History: UseBalanceHistory):
        db.session.add(History)
        db.session.commit()
        return History
    
    @staticmethod
    def get_by_account_id(account_id: int):
        return db.session.query(UseBalanceHistory).filter(UseBalanceHistory.account_id == account_id).first()
    
    @staticmethod
    def get_count_history(account_id: int) -> int:
        return db.session.query(UseBalanceHistory).filter(UseBalanceHistory.account_id == account_id).count()
    
    def get_all_history(self, account_id: int):
        return UseBalanceHistory.query.filter(UseBalanceHistory.account_id == account_id).all()
