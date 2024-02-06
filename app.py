from flask import Flask
from flask_smorest import Api
from domain.db_connect import db

from config.app_constants import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # SQLALCHEMY 에서 사용할 db url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # SQLALCHEMY 이벤트를 처리하는 옵션
app.config["SQLALCHEMY_ECHO"] = True  # ddl을 볼 수 있는 옵션
app.config['DEBUG'] = True  # debug모드 옵션

_db = db
_db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        _db.create_all()

    app.run(host='localhost', port=5000, debug=True)
