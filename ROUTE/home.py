from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def helloFlask():
    return '플라스크 지금부터 시작!'