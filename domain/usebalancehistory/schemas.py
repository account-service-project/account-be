from marshmallow import Schema, fields


class UseBalanceHistorySchema(Schema):
    id = fields.Integer(dump_only=True, required=True)
    use_balance = fields.Integer(required=True)
    current_balance = fields.Integer(required=True)
    # created_date = fields.DateTime(required=True)
    account_id = fields.Integer(required=True)
