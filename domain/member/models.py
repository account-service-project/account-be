from datetime import datetime
from domain.db_connect import db

_db = db


class Member(_db.Model):
    id: int = _db.Column(_db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username: str = _db.Column(_db.String(50), nullable=False)
    email_id: str = _db.Column(_db.String(50), nullable=False, unique=True)
    password: str = _db.Column(_db.String(50), nullable=False)
    phone_number: str = _db.Column(_db.String(50), nullable=False, unique=False)
    created_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now())
    modified_date: datetime = _db.Column(_db.DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, username: str, email_id: str, password: str, phone_number: str):
        self.username = username
        self.email_id = email_id
        self.password = password
        self.phone_number = phone_number

    def __iter__(self):
        yield 'username', self.username
        yield 'email_id', self.email_id
        yield 'password', self.password
        yield 'phone_number', self.phone_number

    @staticmethod
    def from_dto(register_form: dict):
        return Member(
            username=register_form['username'],
            email_id=register_form['email_id'],
            password=register_form['password'],
            phone_number=register_form['phone_number'],
        )
