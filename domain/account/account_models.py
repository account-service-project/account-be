from domain.db_connect import db
from config.constants import INITIAL_BALANCE

_db = db


class Account(_db.Model):
    # __tablename__ = 'account'
    id: int = db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    account_number: str = _db.Column(_db.String(30), unique=True, nullable=False)
    current_balance: float = _db.Column(_db.Float, nullable=False, default=0)
    member_id: int = db.Column(_db.Integer, db.ForeignKey('member.id'), nullable=False)

    def __init__(self, account_number: str, member_id: int):
        self.account_number = account_number
        self.current_balance = INITIAL_BALANCE
        self.member_id = member_id
