from marshmallow import Schema, fields


class AccountSchema(Schema):
    id = fields.Integer(dump_only=True, required=True)
    account_number = fields.String(required=True)
    current_balance = fields.Float(required=True)
    member_id = fields.Integer(required=True)