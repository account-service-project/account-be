from domain.member.models import Member
from domain.member.repository import MemberRepository

from flask_smorest import abort


class MemberService:
    def __init__(self):
        self.repository = MemberRepository()

    def register(self, member: Member):
        self.__register_request_validation_check(member)

        return self.repository.save(member)

    def __register_request_validation_check(self, member: Member) -> None:
        if self.repository.get_by_email_id(member.email_id):
            abort(400, message='this email id is already registered')

        if self.repository.get_by_phone_number(member.phone_number):
            abort(400, message='this phone number is already registered')


