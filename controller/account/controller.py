from flask.views import MethodView
from flask_smorest import Blueprint
from service.account.service import AccountService
from domain.account.schemas import AccountSchema

account_bp = Blueprint('account_controller', 'account_controller', url_prefix='/accounts', description='계좌 개설')

class AccountController(MethodView):
    def __init__(self):
        self.account_service = AccountService()

    @account_bp.response(201, AccountSchema)
    def post(self, member_id: int):
        return self.account_service.create_account(member_id)

    def get(self, member_id: int):
        return self.account_service.get_accounts_list(member_id)
    
    def delete(self, member_id: int, account_id: int):
        return self.account_service.delete_account(member_id, account_id)
    
account_controller_view= AccountController.as_view('account_controller')
account_bp.add_url_rule('/create/<int:member_id>', view_func=account_controller_view, methods=['POST'])
account_bp.add_url_rule('/<int:member_id>', view_func=account_controller_view, methods=['GET'])
account_bp.add_url_rule('/delete/<int:member_id>/<int:account_id>', view_func=account_controller_view, methods=['DELETE'])