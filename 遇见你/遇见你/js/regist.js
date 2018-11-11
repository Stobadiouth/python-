$(document).ready(function () {
    let verifyCode = new GVerify("imgsure");

    $('.a7>input').on('input propertychange',function () {
        let tel=$(this).val();
        if (check_tel(tel)) {
            $(this).next().css('display','none')
        }else {
            $(this).next().css('display','block')
        }
    });
    $('.a9>input:first').on('input propertychange',function () {
        let pwd=$(this).val();
        if (check_pwd(pwd)) {
            $(this).next().css('display','none')
        }else {
            $(this).next().css('display','block')
        }
    });
    $('.a9>input:last').on('input propertychange',function () {
        let pwd=$('.a9>input:first').val();
        let pwd2=$(this).val();
        if (pwd==pwd2) {
            $(this).next().css('display','none')
        }else {
            $(this).next().css('display','block')
        }
    });
    $('.a11').click(function () {
        let imgsure = verifyCode.validate($(".a8>input").val());
        let sex_id=$('[name="sex"]:checked').val();
        let tel=$('.a7>input').val();
        let password=$('.a9>input:first').val();
        let password2=$('.a9>input:last').val();
        if (check_tel(tel) && password==password2 &&check_pwd(password) && imgsure){
            let user={
                "tel":tel,
                "password":password,
                "sex_id":sex_id
            };
            console.log(user);
            $.ajax({
                url:'http://localhost:8000/user/regist/',
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
                        location.href='index.html'
                    }
                    else {
                        $('.error1').css('display','none');
                        $('.error2').css('display','block')
                    }
                },
                error:function (XMLHttpRequest,textStatus,errorThrown) {
                    console.log('nononon');
                    console.log(textStatus)
                }
            })
        }
        else {
            $('.error2').css('display','none');
            $('.error1').css('display','block')
        }
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
    let reg=/^\w{6,16}$/
    if (reg.test(pwd)){
        return true
    }
    return false
}