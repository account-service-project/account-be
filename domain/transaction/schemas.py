from marshmallow import Schema, fields

class HistoryRequest(Schema):
    transaction_type = fields.String(required=True)
    use_balance = fields.Integer(required=True)
    member_id = fields.Integer(required=True)
    account_number = fields.String(required=True)

class HistoryResponse(Schema):
    id = fields.Integer(dump_only=True, required=True)
    transaction_type = fields.String(required=True)
    use_balance = fields.Integer(required=True)
    current_balance = fields.Integer(required=True)
    # created_date = fields.DateTime(required=True)
    account_id = fields.Integer(required=True)