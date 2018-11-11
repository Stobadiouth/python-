from app.dao.position_dao import *
from flask import json

#查找所有的岗位
def check_searchPositon(request):
    res=searchPosition()
    return res

def search_position(request):
    name= request.values['name']
    if name:
        c = select_position(name)
        if c:
            return c
        else:
            return json.jsonify({"statuscode": "公司没有岗位！"})
    else:
        return json.jsonify({"statuscode": "公司不能为空！"})

def select_position(request):
    id= request.values['id']
    if id:
        c = select_idmassage(id)
        if c:
            return c
        else:
            return json.jsonify({"statuscode": "公司没有岗位！"})
    else:
        return json.jsonify({"statuscode": "公司不能为空！"})

#找到所有的职位
def check_searchProfession():
    res=searchProfession()
    return res

#根据搜索的内容找到所有的职位
def check_searchPositionByName(request):
    str=request.values['search']
    print(str)
    res=searchPositionByName(str)
    return res

#根据搜索的内容找到所有的职位
def check_searchPositionById(request):
    id=request.values['id']
    print(id)
    res=searchPositionById(id)
    return res