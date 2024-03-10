from flask import Blueprint

route = Blueprint('route1', __name__, template_folder='routes')


@route.route('/home',methods=['GET'])
def get_as_text_route():
    return 'sdsfasf122421421'
