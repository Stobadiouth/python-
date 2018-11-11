//默认简历为中文简历
let resume_title='中文简历';
let resumes=null;


window.onload=function () {
    let tel=sessionStorage.getItem('telephone');
    //已经登录
    if (tel){
        //传给ajax
        ajax('POST','http://localhost:5000/resume/searchresume',{"telephone":tel},function (result) {
            console.log(result);
            //第一次加载界面
            resumes=result;
            showResume(resumes);

        },sessionStorage.getItem('token'))
        //没有登录
    } else{
        sessionStorage.setItem('from','jianli.html');
        alert('请先登录');
        location.href='login.html'
    }
    //给简历列表添加点击事件
    document.querySelector('.jianli_biaoti').onclick=function (evevt) {
        if (evevt.target.nodeName=="LI"){
            let lis=this.querySelectorAll('li');
            for (let li of lis){
                li.style['border-left']="solid 2px white";
            }
            evevt.target.style['border-left']="solid 2px #00de00";
            resume_title=evevt.target.innerText;
            showResume();
        }

    }
};

//加载界面函数
function showResume() {
    for (let resume of resumes){
        console.log(resume);
        if (resume.resume_title==resume_title) {
            document.querySelector('#user_name').innerHTML=resume.name;
            document.querySelector('#user_miaoshu').innerHTML=`${resume.advantage}`;
            document.querySelector('#user_telephone').innerHTML=resume.telephone;
            document.querySelector('#main_work').innerHTML=`
                <p><img src="../images/简历_分隔图.png" /></p>
                <p class="gongzuo">工作经历</p>
            `;
            for (let j=0;j<resume.jobs.length;j++){
                document.querySelector('#main_work').innerHTML+=`
                    <div>
                    <p>第${j+1}份工作简历</p>
                    <p>公司:${resume.jobs[j].company_name}</p>
                    <p class="gongzuo">部门:${resume.jobs[j].department}</p>
                    <p class="gongzuo">职位:${resume.jobs[j].position_name}</p>
                    <p class="gongzuo">主要工作:${resume.jobs[j].work_content}</p>
                    </div>
            `
            }
            document.querySelector('#main_edu').innerHTML=`
                <p><img src="../images/简历_分隔图.png" /></p>
                <p class="gongzuo">教育经历</p>
                <p class="imgadd"><img src="../images/简历_添加.png" /></p>
            `;
            for (let j=0;j<resume.edus.length;j++){
                document.querySelector('#main_edu').innerHTML+=`
                    <div>
                    <p>第${j+1}份教育简历</p>
                    <p>学历:${resume.edus[j].education}</p>
                    <p class="gongzuo">主修:${resume.edus[j].major}</p>
                    <p class="gongzuo">学校:${resume.edus[j].school_name}</p>
                    </div>
                `
            }
            break
        }
    } 
}