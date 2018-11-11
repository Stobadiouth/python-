$(document).ready(function(){
    //判断是否记住密码
    if ($.cookie("rmbUser")=="true"){
        $("#chk_log").attr('checked',true);
        $('.tel').val($.cookie('telephone'));
        $('.mima').val($.cookie(('password')));
    }
    //点击登录
    $('.ljdl').click(function () {
        let tel=$('.tel').val();
        let password=$('.mima').val();
        if (check_pwd(password) && check_tel(tel)) {
            user={
                "tel":tel,
                "password":password
            };
            console.log(user);
            $.ajax({
                url:'http://localhost:8000/user/login/',
                type:"POST",
                data:JSON.stringify(user),
                dataType:"json",
                contentType:"application/json",
                success:function (response,textStatus,xhr) {

                    console.log(response);
                    console.log(textStatus);
                    // console.log(request.getAllResponseHeaders())
                    console.log(xhr.getResponseHeader('token'));
                    if (response['id']){
                        sessionStorage.setItem('id',response['id']);
                        localStorage.setItem('token',xhr.getResponseHeader('token'));
                        //记住用户名和密码
                        Save(tel,password);
                        location.href='index.html';
                    }
                    else {
                        $('.error').css('display','block')
                    }
                },
                error:function (XMLHttpRequest,textStatus,errorThrown) {
                    console.log('nononon');
                    console.log(textStatus)
                }
            })
        }
        else {
            $('.error').css('display','block')
        }
    });
//    点击注册
    $('.mfzc').click(function () {
        location.href='regist.html'
    })
});
function check_tel(tel) {
    let reg=/^\d{11}$/;
    if (reg.test(tel)) {
        return true
    }
    return false
}
function check_pwd(pwd) {
    let reg=/^\w{6,16}$/;
    if (reg.test(pwd)){
        return true
    }
    return false
}

//记住用户名密码
function Save(tel,pwd) {
    if ($("#chk_log").prop("checked")) {
        //设置一个小时的cookie
        let now = new Date();
        now.setTime(now.getTime() + 60* 60 * 1000);
        $.cookie("rmbUser", "true", { expires: now }); //存储一个带7天期限的cookie
        $.cookie("telephone", tel, { expires: now });
        $.cookie("password", pwd, { expires: now });
    }
    else {
        $.cookie("rmbUser", "false", { expire: -1 });
        $.cookie("telephone", "", { expires: -1 });
        $.cookie("password", "", { expires: -1 });
    }
}
