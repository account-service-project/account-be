from flask import Flask
from flask_smorest import Api
from domain.db_connect import db
from domain.member.models import Member
from controller.member.member_controller import member_bp
from controller.account.controller import account_bp
from controller.transaction.controller import transaction_bp

from config.app_constants import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['API_TITLE'] = 'account api'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_TITLE'] = 'account api'
app.config['OPENAPI_VERSION'] = '3.1.3'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # SQLALCHEMY 에서 사용할 db url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # SQLALCHEMY 이벤트를 처리하는 옵션
app.config["SQLALCHEMY_ECHO"] = True  # ddl을 볼 수 있는 옵션
app.config['DEBUG'] = True  # debug모드 옵션

_db = db
_db.init_app(app)
api = Api(app)
api.register_blueprint(member_bp)
api.register_blueprint(account_bp)
api.register_blueprint(transaction_bp)

if __name__ == '__main__':
    with app.app_context():
        _db.create_all()

    app.run(host='localhost', port=5000, debug=True)
