from flask import Blueprint,request,make_response,json
from app.utils.utils_token import *
from app.service.user_service import *


user=Blueprint('user',__name__)

@user.route('/')
def index():
    return '用户首页'


# 登录
@user.route('/login',methods=['GET','POST'])
def login():
    if str(request.method)=="GET":
        res = check_login(request)
        if res == '201':
            response = make_response()
            token = send_token(request.values['tel'])
            response.headers['token'] = token
            response.data = json.dumps({"statusCode": '201'})
            return response
        else:
            return '404'
    elif str(request.method)=="POST":
        userid=request.json['tel']
        password = request.json['password']
        if userid and password:
            res=check_login(userid)
            if len(res):
                data_password=res[0]['password']
                if check_password_hash(data_password, password):
                # if data_password==password:
                    response = make_response()
                    # 签发token
                    token = send_token(userid)
                    result = {
                        "token": token,
                        "tel": userid,
                        "statusCode": "201"
                    }
                    # response.headers['token']=token
                    response.data = json.dumps(result)
                    return response
                else:
                    return json.dumps({"statusCode": "401"})#密码不正确
            else:
                return json.dumps({"statusCode": "402"})
        else:
            return json.dumps({"statusCode": "403"})#用户名或密码为空

#注册
@user.route('/regist',methods=['GET','POST'])
def regist():
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
        res=check_regist(request)
        if res==1:
            token=send_token(request.values['tel'])
            return json.jsonify({"status_code":'202'}),200,{"token":token}#注册成功
        elif res==0:
            return '403'#注册失败
        else:
            return '404'#信息不正确


# 查看用户信息
@user.route('/show',methods=['GET','POST'])
@check_token()
def show():
    if str(request.method)=='GET':
        pass
    elif str(request.method)=='POST':
        res=showbyid(request)
        if res:
            return json.jsonify(res)
        else:
            return '没取到信息'


# 修改密码
@user.route('/updata')
@check_token()
def updata():
    res=updatapwd(request)
    if res==0:
        return '修改失败'
    elif res==1:
        return '修改成功'