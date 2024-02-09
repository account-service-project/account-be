from flask.views import MethodView
from flask_smorest import Blueprint

from domain.transaction.models import UseBalanceHistory
from service.transaction.history_service import HistoryService
from domain.transaction.schemas import HistoryRequest, HistoryResponse
transaction_bp = Blueprint('history_controller', 'history_controller', url_prefix='/accounts/transaction', description='거래내역')

@transaction_bp.route('/')
class WithdrawHistoryController(MethodView):
    def __init__(self):
        self.history_service = HistoryService()
    @transaction_bp.arguments(HistoryRequest)
    @transaction_bp.response(200, HistoryResponse)
    def post(self, new_history: HistoryRequest):
        return self.history_service.save_use_balance_history(new_history)
    
    @transaction_bp.response(200, HistoryResponse(many=True))
    def get(self, account_id: int):
        return self.history_service.get_account_history(account_id)
    
history_controller_view = WithdrawHistoryController.as_view('history_controller')
transaction_bp.add_url_rule('/<int:account_id>', view_func=history_controller_view, methods=['GET'])
# transaction_bp.add_url_rule('/', view_func=history_controller_view, methods=['POST'])
