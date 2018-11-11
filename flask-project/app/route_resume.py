from flask import Blueprint,request,json
from app.service.resume_service import *
from app.utils.utils_token import *

resume=Blueprint('resume',__name__)

# 添加基本简历
@resume.route('/create',methods=['GET','POST'])
@check_token()
def create():
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
       res=check_addbase(request)
       if res==0:
           return '404'#添加失败
       elif res==1:
           return '202'#添加成功

#添加工作简历
@resume.route('/createjob',methods=['GET','POST'])
def job():
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
       res=check_addjob(request)
       if res==0:
           return '404'#添加失败
       elif res==1:
           return '202'#添加成功

#添加教育简历
@resume.route('/createedu',methods=['GET','POST'])
def edu():
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
       res=check_addedu(request)
       if res==0:
           return '404'#添加失败
       elif res==1:
           return '202'#添加成功

#完善修改简历
@resume.route('/updata',methods=['GET','POST'])
def updata():
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
       res=check_updata(request)
       if res==0:
           return '404'#添加失败
       elif res==1:
           return '202'#添加成功

#查看简历
@resume.route('/select',methods=['GET','POST'])
def select():
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
       res=check_search(request)
       if res:
           return json.jsonify(res)#查询成功
       else:
           return '404' #查询失败

#删除简历
@resume.route('/delete',methods=['GET','POST'])
@check_token()
def delete():
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
       res=check_delete(request)
       if res:
           return '202'#删除成功
       else:
           return '404' #删除失败

# 查找简历
@resume.route('/searchresume',methods=['GET','POST'])
@check_token()
def searchResume(telephone):
    if str(request.method)=="GET":
        pass
    elif str(request.method)=="POST":
        # token=request.headers['token']
        print(telephone)
        res=check_searchResumeBasic(telephone)
        return json.dumps(res)