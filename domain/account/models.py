from datetime import datetime
from domain.db_connect import db
from config.constants import INITIAL_BALANCE

_db = db


class Account(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    account_number: str = _db.Column(_db.String(30), unique=True, nullable=False)
    current_balance: float = _db.Column(_db.Float, nullable=False, default=INITIAL_BALANCE)
    member_id: int = _db.Column(_db.Integer, _db.ForeignKey('member.id'), nullable=False)
    # member_id: int = _db.relationship('Member', db.ForeignKey('member.id'), nullable=False) # debug
    created_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now())
    modified_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, account_number: str, member_id: int):
        self.account_number = account_number
        self.current_balance = INITIAL_BALANCE
        self.member_id = member_id

    def __iter__(self):
        yield 'id', self.id
        yield 'account_number', self.account_number
        yield 'current_balance', self.current_balance
        yield 'member_id', self.member_id
        yield 'created_date', self.created_date
        yield 'modified_date', self.modified_date