from datetime import datetime
from domain.db_connect import db
from config.constants import INITIAL_BALANCE, INITIAL_USE_BALANCE

_db = db


class UseBalanceHistory(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    use_balance: int = _db.Column(_db.Integer, nullable=False, default=INITIAL_USE_BALANCE)
    current_balance: int = _db.Column(_db.Integer, nullable=False, default=INITIAL_BALANCE)
    created_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now())
    account_id: int = _db.Column(_db.Integer, _db.ForeignKey('account.id'), nullable=False)
    modified_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, account_id: int, created_date: datetime, use_balance: int, current_balance: int):
        self.use_balance = use_balance
        self.current_balance = current_balance
        self.account_id = account_id
        self.created_date = created_date

    def __iter__(self):
        yield 'id', self.id
        yield 'use_balance', self.use_balance
        yield 'current_balance', self.current_balance
        yield 'created_date', self.created_date
        yield 'modified_date', self.modified_date
