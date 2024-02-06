from domain.db_connect import db
from domain.member.models import Member


class MemberRepository:
    @staticmethod
    def save(member: Member):
        db.session.add(member)
        db.session.commit()
        return member

    @staticmethod
    def get_by_email_id(email_id: str):
        return db.session.query(Member).filter(Member.email_id==email_id).first()

    @staticmethod
    def get_by_phone_number(phone_number: str):
        return db.session.query(Member).filter(Member.phone_number==phone_number).first()