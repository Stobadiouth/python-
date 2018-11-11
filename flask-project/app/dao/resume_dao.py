from . import *
from app.dao.resume_sql import *

#添加基本简历
def addResumeBase(base_resume):
    try:
        res = 0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor()
        print(base_resume)
        sql1=do_sql["getUserid"].format(base_resume['user_id'])
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql1)
        res = cursor.fetchall()
        sql = do_sql["addResumeBase"].format(base_resume['title'], base_resume['name'],
                                             base_resume['birth'],res[0]['id'])
        res = cursor.execute(sql)
        uid = connect.insert_id()
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

def addResumejob(resume_job):
    try:
        res = 0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor()
        print(resume_job)
        sql1= do_sql["addResumejob"].format(resume_job['cname'],resume_job['pname'],resume_job['resume_basic_id'])
        cursor.execute(sql1)
        uid = connect.insert_id()
        print(uid)
        sql2=do_sql["updataBasic"].format(uid,resume_job['resume_basic_id'])
        res=cursor.execute(sql2)
        connect.commit()
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

def addResumeedu(resume_edu):
    try:
        res = 0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor()
        print(resume_edu)
        sql= do_sql["addResumeedu"].format(resume_edu['school'],resume_edu['resume_basic_id'])
        res=cursor.execute(sql)
        uid = connect.insert_id()
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

def updataResume(resume_updata):
    try:
        res = 0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor()
        print(resume_updata)
        sql= do_sql["updataResume"].format(resume_updata['table'],resume_updata['term'],
                                           resume_updata['new'],resume_updata['id'])
        res=cursor.execute(sql)
        uid = connect.insert_id()
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

def searchResume(id):
    try:
        res = 0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor()
        print(id)
        sql= do_sql["searchResume"].format(id)
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

def deleteResume(id):
    try:
        res=0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor()
        print(id)
        sql= do_sql["deleteResume"].format(id)
        # res=cursor.callproc(do_sql["deleteResume"].format(id))
        res=cursor.execute(sql)
        connect.commit()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

#查询基本简历
def searchResumeBasic(id):
    try:
        res=0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        print(id)
        sql= do_sql["searchResumeBasic"].format(id)
        cursor.execute(sql)
        res=cursor.fetchall()
        connect.commit()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

#查询工作简历
def searchResumeJob(id):
    try:
        res=0
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        print(id)
        sql= do_sql["searchResumeJob"].format(id)
        cursor.execute(sql)
        res=cursor.fetchall()
        connect.commit()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res

#查询教育简历
def searchResumeEdu(id):
    try:
        res=()
        cursor = None
        connect = None
        connect = creatConnet()
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        print(id)
        sql= do_sql["searchResumeEdu"].format(id)
        cursor.execute(sql)
        res=cursor.fetchall()
        connect.commit()
        print(res)
    except Exception as ex:
        print(ex)
    finally:
        if cursor:
            cursor.close()
        if connect:
            connect.close()
        return res