from . import *
from app.dao.user_sql import *
def addUser(user):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnet()
        cursor=connect.cursor()
        print(user)
        sql = do_sql["addUser"] .format(user['tel'], user['password'])
        res=cursor.execute(sql)
        uid=connect.insert_id()
        print(uid)
        connect.commit()
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

def updataUser(user):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnet()
        cursor=connect.cursor()
        print(user)
        sql = do_sql["updatePassword"] .format(user['newpwd'],user['id'])
        res=cursor.execute(sql)
        connect.commit()
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

def getUserById(userid):
    try:
        res=0
        cursor=None
        connect=None
        connect=creatConnet()
        cursor=connect.cursor(cursor=pymysql.cursors.DictCursor)
        print(userid)
        sql = do_sql["getUserById"] .format(userid)
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