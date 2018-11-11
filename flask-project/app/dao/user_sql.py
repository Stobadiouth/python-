do_sql={
    "addUser":"insert into user(telephone,password,regist_date) values('{0}','{1}',CURDATE())",
    "getUserById":"SELECT * from user where telephone='{0}'",
    "delUserById":"",
    "updatePassword":"UPDATE user set password='{0}' where id='{1}'"
}