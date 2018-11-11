window.onload=function () {
    let user_tel=sessionStorage.getItem('telephone');
    if (user_tel){
        document.querySelector('#nologin ul').innerHTML=`
                <li><a href="pages/login.html">${user_tel} &nbsp;|</a></li>
                <li><a href="">退出</a></li>
        `
        document.querySelector('#nologin ul').children[1].onclick=function () {
            //清空session
            sessionStorage.clear();
            this.parentElement.innerHTML=`
                <li><a href="pages/login.html">登录 &nbsp;|</a></li>
                <li><a href="pages/regist.html">注册</a></li>
            `
        }
    }
    sessionStorage.setItem('from','job.html');
    let id=sessionStorage.getItem('position_id');
    //渲染界面
    showMesseage(id);
    //投递简历
    document.querySelector('#btn_apply').onclick=function () {
        if(user_tel){
            alert('选择你的简历')
        }else {
            alert('你还没有登录')
        }
    }



};

function showMesseage(id) {
    ajax('GET','http://localhost:5000/position/searchpositionbyid',{"id":id},function (result) {
        console.log(result);
        let position=result[0];
        document.querySelector('.jobname_left').innerHTML=`
            <ul>
            	<li id="job_name">${position.name}</li>
                <li id="job_info">${position.job_nature}</li>
                <li id="job_level">${position.tags}</li>
                <li id="job_publish_time">发布时间：${position.publish_date}</li>
            </ul>
        `
        document.querySelector('.jobinfo_right').innerHTML=`
            <p>
                <img src="../images/公司logo.png" height="68" width="67"/>
                <span style="font-size: 16px; position: relative; top: 6px;" id="company_name">${position.company_name}</span><img src="../images/认证图标.png" height="25" width="22"/></p>
            <p>
                <img src="../images/职位详情图标1.png" height="30" width="31"/>
                <span id="profession_name">${position.profession_name}</span>
            </p>
            <p><img src="../images/职位详情图标2.png" height="30" width="31"/>
                <span id="company_stage">未融资</span>
            </p>
            <p><img src="../images/职位详情图标3.png" height="30" width="31"/>
                <span id="company_acount">150-500</span>
            </p>
        `
        document.querySelector('.jobinfo_left').innerHTML=`
            <p>我们的优点：${position.attraction}</p>
            <p>工作经验要求：${position.years_working}</p>
            <p>薪水：${position.salary}</p>
            <p>所在地：${position.city_name}</p>
        `
    })
}