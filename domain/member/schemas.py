from marshmallow import Schema, fields

from domain.member.models import Member


class RegisterMemberRequest(Schema):
    username = fields.String(required=True)
    email_id = fields.String(required=True)
    password = fields.String(required=True)
    phone_number = fields.String(required=True)


class RegisterMemberResponse(Schema):
    id = fields.Integer(dump_only=True, required=True)
    username = fields.String(required=True)
    email_id = fields.String(required=True)
    phone_number = fields.String(required=True)

