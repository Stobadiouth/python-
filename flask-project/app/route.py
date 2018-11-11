from app.app import app
from app.route_user import *
from app.route_resume import *
from app.route_position import *
from flask import jsonify,make_response

@app.route('/')
def index():
    return '这是首页'

@app.route('/test/',methods=['GET','POST'])
def test():
    if request.method=='GET':
        print(request.user_agent.browser)
        res={"status":"200"}
        return jsonify(res)

app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(resume,url_prefix='/resume')
app.register_blueprint(position,url_prefix='/position')

@app.errorhandler(404)
def miss(e):
    return '404'

@app.errorhandler(500)
def error(e):
    return '500'