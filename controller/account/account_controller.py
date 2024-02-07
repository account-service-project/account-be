from flask.views import MethodView
from flask_smorest import Blueprint

from service.account.account_service import AccountService
from domain.account.account_schemas import AccountSchema

account_bp = Blueprint('account_controller', 'account_controller', url_prefix='/accounts', description='계좌 개설')


@account_bp.route('/create/<int:member_id>')
class AccountController(MethodView):
    def __init__(self):
        self.account_service = AccountService()

    @account_bp.arguments(AccountSchema)
    @account_bp.response(201, AccountSchema)
    def post(self, member_id: int):
        return self.account_service.create_account(member_id)

