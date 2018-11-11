from werkzeug.security import generate_password_hash,check_password_hash
from app.dao.user_dao import *


def check_login(userid):
    res=getUserById(userid)
    return res

def check_regist(request):
    userid = request.values['tel']
    password = request.values['password']
    confirm = request.values['confirm']
    result=None
    if userid and password and password == confirm:
        sha1_password = generate_password_hash(password, method='pbkdf2:sha1:200', salt_length=8)
        user = {
            "tel": userid,
            "password": sha1_password
        }
        result= addUser(user)
    return result

def updatapwd(request):
    id=request.headers['id']
    newpwd=request.headers['newpwd']
    user={
        "id":id,
        "newpwd":newpwd
    }
    res=updataUser(user)
    return res

def showbyid(request):
    id=request.values['tel']
    user={"tel":id}
    res=getUserById(user)
    return res


if __name__ == '__main__':
    password = generate_password_hash('', method='pbkdf2:sha1:200', salt_length=8)
    print(password)