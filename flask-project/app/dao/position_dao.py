from . import *
from app.dao.position_sql import *

#找到所有的岗位
def searchPosition():
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnet()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        sql = do_sql["searchPosition"]
        cursor.execute(sql)
        res=cursor.fetchall()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

def select_position(name):
    try:
        res=0
        connect=creatConnet()
        cursor = connect.cursor()
        my_sql=do_sql["select_position"].format(name)
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(my_sql)
        res= cursor.fetchall()
        connect.commit()
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

def select_idmassage(id):
    try:
        res=0
        connect=creatConnet()
        cursor = connect.cursor()
        my_sql=do_sql["select_id"].format(id)
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(my_sql)
        res = cursor.fetchall()
        connect.commit()
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

#找到所有的行业
def searchProfession():
    try:
        res=0
        connect=creatConnet()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        my_sql=do_sql["searchProfession"]
        cursor.execute(my_sql)
        res = cursor.fetchall()
        connect.commit()
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

#根据搜索内容找到所有的岗位
def searchPositionByName(str):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnet()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        sql = do_sql["searchPositionByName"].format(str,str)
        cursor.execute(sql)
        res=cursor.fetchall()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

#根据id查找岗位信息
def searchPositionById(id):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnet()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        sql = do_sql["searchPositionById"].format(id)
        cursor.execute(sql)
        res=cursor.fetchall()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res