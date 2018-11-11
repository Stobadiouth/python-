do_sql={
    "addResumeBase":"INSERT into resume_basic(resume_title,name,birth_date,user_id)VALUES('{0}','{1}','{2}','{3}')",
    "getUserid":"select id from user where telephone='{0}'",
    "addResumejob":"insert into resume_jobs(company_name,position_name,resume_basic_id)values('{0}','{1}','{2}')",
    "updataBasic":"UPDATE resume_basic set position_now='{0}' WHERE id='{1}'",
    "addResumeedu":"insert into resume_education(school_name,resume_basic_id) values('{0}','{1}')",
    "updataResume":"UPDATE {0} set {1}='{2}' WHERE id='{3}'",
    "searchResume":"select * from  resume_basic  left JOIN resume_jobs on resume_basic.id =resume_jobs.resume_basic_id LEFT "
                   "JOIN resume_education on resume_education.resume_basic_id=resume_basic.id "
                   "where resume_basic.user_id= (SELECT id from user WHERE telephone='{0}')",
    "deleteResume":"call delResume('{0}')",
    "searchResumeBasic":"select USER.id,USER.telephone,resume_basic.advantage,resume_basic.id as resume_id,resume_basic.name,resume_basic.resume_title "
                        "from user inner join resume_basic on user.id=resume_basic.user_id "
                        "where user.telephone='{0}'",
    "searchResumeJob":"select * from resume_jobs where resume_basic_id={0}",
    "searchResumeEdu":"select * from resume_education where resume_basic_id={0}"
}