from flask import Blueprint,request,json
from app.service.position_service import *

position=Blueprint('position',__name__)

#查询岗位列表
@position.route('/search',methods=['GET','POST'])
def search():
    if str(request.method)=="GET":
        res=check_searchPositon(request)
        if res:
            for p in res:
                p['publish_date'] = str(p['publish_date'])
            return json.dumps(res)
        else:
            return '404'  # 为空
    elif str(request.method)=="POST":
       res=check_searchPositon(request)
       if res:
           return json.jsonify(res)
       else:
           return '404'#为空

# 根据公司名称
@position.route('/searchjob',methods=['POST','GET'])  #/user/add
def search_job():
    a=search_position(request)
    return json.jsonify(a)

#很具岗位id查询
@position.route('/select_position',methods=['POST','GET'])  #/user/add
def search_id():
    a=select_position(request)
    return json.jsonify(a)

#查询所有的行业
@position.route('/profession',methods=['GET','POST'])
def profession():
    if str(request.method)=="GET":
        res=check_searchProfession()
        print(res)
        return json.dumps(res)
    elif str(request.method)=="POST":
       res=check_searchPositon(request)
       if res:
           return json.jsonify(res)
       else:
           return '404'#为空

#根据搜索查询所有的岗位
@position.route('/searchposition',methods=['GET','POST'])
def searchposition():
    if str(request.method)=="GET":
        res=check_searchPositionByName(request)
        for p in res:
            p['publish_date'] = str(p['publish_date'])
        print(res)
        return json.dumps(res)
    elif str(request.method)=="POST":
       res=check_searchPositon(request)
       if res:
           return json.jsonify(res)
       else:
           return '404'#为空

#根据搜索查询所有的岗位
@position.route('/searchpositionbyid')
def searchpositionbyid():
    res=check_searchPositionById(request)
    for p in res:
        p['publish_date'] = str(p['publish_date'])
    print(res)
    return json.dumps(res)
