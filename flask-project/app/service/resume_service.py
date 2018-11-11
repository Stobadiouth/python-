from app.dao.resume_dao import *
import jwt
from app.app import app

# 添加基本简历
def check_addbase(requst):
    token = requst.headers['token']
    decoded = jwt.decode(token, app.config['SECRET_KEY'], audience='webkit', algorithms=['HS256'])
    user_id=decoded['user_id']
    title=requst.values['title']
    name=requst.values['name']
    birth=requst.values['birth']
    base_resume={
        "title":title,
        "name":name,
        "birth":birth,
        "user_id":user_id
    }
    res=addResumeBase(base_resume)
    return res

# 添加工作简历
def check_addjob(requst):
    cname=requst.values['cname']
    pname=requst.values['pname']
    basic_id=requst.values['resume_basic_id']
    resume_job={
        "cname":cname,
        "pname":pname,
        "resume_basic_id":basic_id
    }
    res=addResumejob(resume_job)
    return res

# 添加教育简历
def check_addedu(requst):
    school=requst.values['school']
    basic_id=requst.values['resume_basic_id']
    resume_edu={
        "school":school,
        "resume_basic_id":basic_id
    }
    res=addResumejob(resume_edu)
    return res

#更新完善简历
def check_updata(requst):
    table=requst.values['table']
    term=requst.values['term']
    new=requst.values['new']
    id=requst.values['id']
    resume_updata = {
        "table": table,
        "term": term,
        "new": new,
        "id": id
    }
    res=updataResume(resume_updata)
    return res

#查找简历信息
def check_search(requst):
    id=requst.values['tel']
    res=searchResume(id)
    return res

#删除简历信息
def check_delete(requst):
    token = requst.headers['token']
    decoded = jwt.decode(token, app.config['SECRET_KEY'], audience='webkit', algorithms=['HS256'])
    id=decoded['user_id']
    res=deleteResume(id)
    return res

#查找简历信息
def check_searchResumeBasic(id):
    res=searchResumeBasic(id)
    if len(res):
        for i in range(len(res)):
            jobs=searchResumeJob(res[i]['resume_id'])
            edus = searchResumeEdu(res[i]['resume_id'])
            res[i]['jobs']=jobs
            res[i]['edus']=edus
    return res


