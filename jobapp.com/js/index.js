//每页5条数据
let page_size=5;
//总页数
let page_count=0;

//定义一个condition
let condition={
    "search":"",//搜索内容
    "select_profession":"",//选择职业
    "order":"",//排序
    "page_index":1//页码
};
//所有岗位数据
let all_positions=null;

//需要的岗位数据
let result_positions=null;

//找到行业的span
let hangye=document.querySelector('#hangye_neirong');
//获取底部页码
let page=document.querySelector('#lin-page-index');
//找到主界面
let main=document.querySelector('#job_mian');
//找到页码
let link_page=document.querySelector('#lin-page-index');
//找到搜索按钮
let btn_search=document.querySelector('#btnSearch');
//找到岗位模块
let div_position=document.querySelector('#job_mian');

//第一次加载页面
window.onload=function () {
    let user_tel=sessionStorage.getItem('telephone');
    //是否登录
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
    //加载所有的行业
    getProfessions();

    //第一次加载所有的岗位
    getPositions();

    //点击搜索按钮
    btn_search.onclick=function(event){
        alert(event.target.previousElementSibling.value.trim());
        condition.search=event.target.previousElementSibling.value.trim();
        searchPosition()
    };

    //给行业添加点击事件
    hangye.onclick=function (event) {
        let as=this.querySelectorAll('a');
        for (let a of as){
            a.style.background='#F8F8FF';
            a.style.color='black'
        }
        event.target.style.background='green';
        event.target.style.color='white';
        condition.select_profession=event.target.innerText;
        condition.page_index=1;
        change_condition(condition)
    };

    //给页码添加点击事件
    link_page.onclick=function (event) {
        condition.page_index=event.target.innerText;
        change_condition(condition);
    }

};

//搜索时加载所有岗位
function searchPosition() {
    ajax('GET','http://localhost:5000/position/searchposition',{"search":condition.search},function (position) {
        console.log(position);
        all_positions=position;
        condition.page_index=1;
        condition.select_profession='';
        change_condition(condition);
        getProfessions();
    })
}

//第一次加载所有的行业
function getProfessions() {
    ajax('GET','http://localhost:5000/position/profession',null,function (professions) {
        hangye.innerHTML=`
            <a href="javascript:void 0" id="0">不限</a>
        `;
        for (let pro of professions){
            hangye.innerHTML+=`
                
                <a href="javascript:void 0" id="0">${pro.name}</a>
            `
        }
    })
}

//第一次获取所有的岗位
function getPositions() {
    ajax('GET','http://localhost:5000/position/search',null,function (positions) {
        console.log(positions);
        all_positions=positions;
        change_condition(condition);
    })
}

//根据需求改变页面
function change_condition(condition) {
    result_positions=[];
    if (condition.select_profession && condition.select_profession!='不限') {
        //遍历数据
        for (let pro of all_positions) {
            if (pro.profession_name == condition.select_profession) {
                result_positions.push(pro)
            }
        }
    }    else {
        result_positions=all_positions
    } 
    page_count=Math.ceil(result_positions.length/page_size);
    loadPage(page_count);
    let start=(condition.page_index-1)*page_size;
    let end=condition.page_index*page_size-1;
    console.log(start,end);
    loadPosition(start,end)
}


//加载当前页码的岗位，并给岗位添加点击事件
function loadPosition(start,end) {
    let page_position=[];
    //需求岗位的长度如果大于end正常加载，否则end等于长度减一
    end=result_positions.length>end?end:result_positions.length-1;
    for (let i=start;i<=end;i++){
        page_position.push(result_positions[i])
    }
    main.innerHTML='';
    for ( let p of page_position) {
        console.log(p.publish_date);
        let time=format_date(p.publish_date);
        main.innerHTML += `
            <div class="job-item" id="${p.id}">
                <div class="job-item-top">
                    <div class="job-item-top-left">
                        <span style="color: #00b38a">${p.name}【${p.city_name}】 ${time}</span> <br>
                        <span style="color: red">${p.salary}</span> 经验1-3年/ 本科
                    </div>
                    <div class="job-item-top-center">
                        <span style="color: #00b38a">${p.company_name}</span> <br>
                        企业服务/成长型
                    </div>
                    <div class="job-item-top-right">
                        icon
                    </div>
                </div>
                <div class="job-item-bottom">
                    <div class="job-item-bottom-left">
                        <button>web</button>
                        <button>脚本</button>
                    </div>
                    <div class="job-item-bottom-right">bb</div>
                </div>
            </div>
        `
    }
    //给当前页面的岗位添加点击事件
    let positions=document.querySelectorAll('#job_mian>div');
    for (let position of positions){
        position.onclick=function () {
            for (let po of page_position){
                if (po.id==this.id){
                    sessionStorage.setItem('position_id',po.id);
                    location.href='pages/job.html';
                    break
                }
            }
        }
    }
}

//加载底部页码
function loadPage(page_count) {
    page.innerHTML='';
    for (let i=1;i<=page_count;i++){
        page.innerHTML+=`
            <a href="javascript:void 0">${i}</a>
        `
    }
}

//格式化时间
function format_date(str) {

    let date=new Date(str);

    let now=new Date();

    let days=parseInt(((now-date)/1000)/(24*60*60));
    console.log(days);
    if(days>3){
        return str.split(' ')[0];
    }else {
        return days+'天前发布'
    }
}