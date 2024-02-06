from flask.views import MethodView
from flask_smorest import Blueprint

from domain.member.models import Member
from service.member.member_service import MemberService
from domain.member.schemas import RegisterMemberRequest, RegisterMemberResponse

member_bp = Blueprint('member_controller', 'member_controller', url_prefix='/members', description='회원가입')


@member_bp.route('/register')
class MemberController(MethodView):

    def __init__(self):
        self.member_service = MemberService()

    @member_bp.arguments(RegisterMemberRequest)
    @member_bp.response(200, RegisterMemberResponse)
    def post(self, form):
        member = Member.from_dto(form)
        return self.member_service.register(member)
