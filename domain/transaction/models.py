from datetime import datetime
from domain.db_connect import db
from config.constants import INITIAL_BALANCE, INITIAL_USE_BALANCE

_db = db


class UseBalanceHistory(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    transaction_type: str = _db.Column(_db.String(30), nullable=False, default=None)
    use_balance: int = _db.Column(_db.Integer, nullable=False, default=INITIAL_USE_BALANCE)
    current_balance: int = _db.Column(_db.Integer, nullable=False, default=INITIAL_BALANCE)
    created_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now())
    account_id: int = _db.Column(_db.Integer, _db.ForeignKey('account.id'), nullable=False)
    modified_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, transaction_type: str, account_id: int, use_balance: int, current_balance: int):
        self.transaction_type = transaction_type
        self.use_balance = use_balance
        self.current_balance = current_balance
        self.account_id = account_id

    def __iter__(self):
        yield 'id', self.id
        yield 'transaction_type', self.transaction_type
        yield 'use_balance', self.use_balance
        yield 'current_balance', self.current_balance
        yield 'created_date', self.created_date
        yield 'modified_date', self.modified_date
