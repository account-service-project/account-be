from flask_smorest import abort
from domain.transaction.repository import UseBalanceHistoryRepository
from domain.transaction.models import UseBalanceHistory
from domain.account.repository import AccountRepository
from domain.transaction.schemas import HistoryRequest

from config.constants import AMOUNT_ERROR_MESSAGES, TRANSACTION_TYPE_ERROR
from flask import jsonify

class HistoryService:
    def __init__(self):
        self.repository = UseBalanceHistoryRepository()
        self.account_repository = AccountRepository()
    
    def check_amount(self, amount: int):
        if amount <= 0:
            abort(400, message=AMOUNT_ERROR_MESSAGES)
    
    def check_transaction_type(self, transaction_type: str):
        if transaction_type not in ['deposit', 'withdraw']:
            abort(400, message=TRANSACTION_TYPE_ERROR)

    def transaction_request_validation_check(self, request: HistoryRequest):
        self.check_amount(amount=request['use_balance'])
        self.check_transaction_type(transaction_type=request['transaction_type'])
    
    def cal_current_balance(self, account_id: int, amount: int, transaction_type: str):
        account = self.account_repository.get_by_account_id(account_id)
        if transaction_type == "deposit":
            return account.current_balance + amount
        
        cur_bal = account.current_balance - amount
        return cur_bal if cur_bal > 0 else abort(400, message='amount must be greater than current balance')

    def update_account_current_balance(self, cur_bal: int, account_id: int):
        account = self.account_repository.get_by_account_id(account_id)
        account.current_balance = cur_bal
        self.account_repository.save(account)

    def save_use_balance_history(self, request: HistoryRequest):
        account = self.account_repository.get_by_account_number(request['account_number'])
        self.transaction_request_validation_check(request)

        cur_bal = self.cal_current_balance(account_id=account.id, amount=request['use_balance'], transaction_type=request['transaction_type'])
        self.update_account_current_balance(cur_bal, account.id)
        new_history = UseBalanceHistory(transaction_type=request['transaction_type'], use_balance=request['use_balance'], current_balance=cur_bal, account_id=account.id)
        return self.repository.save(new_history)

    def get_account_history(self, account_id: int):
        if self.repository.get_count_history(account_id=account_id) < 1:
            abort(400, "no history in")
            
        history_obj =  self.repository.get_all_history(account_id=account_id)
        history_list = [dict(history) for history in history_obj]
        
        return history_list

    
    
