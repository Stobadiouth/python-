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

$(document).ready(function () {
    //加载行业
    getProfessions();
    //给行业添加点击事件
    professionsClick();
    //第一次加载页面
    getPositions();
    //给页码添加点击事件
    indexClick();
    //点击搜索
    searchPositions();
});

//加载行业
function getProfessions() {
    $.ajax({
        url:"http://localhost:5000/position/profession",
        async:true,
        type:"GET",
        dataType:"json",
        success:function (result) {
            console.log(result);
            let hangye=$('#hangye_neirong');
            hangye.html("<a href=\"javascript:void 0\" id=\"0\">不限</a>");
            for (let profession of result){
                hangye.append(`<a href=\"javascript:void 0\" id=\"0\">${profession.name}</a>`)
            }
        }
    });
}

//给行业添加点击事件
function professionsClick() {
    //改变样式
    $('#hangye_neirong').on('click','a',function () {
        $(this).css({'backgroundColor':'green','color':'white'});
        $(this).siblings().css({'background':'#F8F8FF','color':'black'})
    }).on('click','a',function () {
        condition.select_profession=$(this).text();
        condition.page_index=1;
        //获取当前的result_positions
        getResult()
    });
}

//第一次加载页面
function getPositions() {
    $.ajax({
        url:"http://localhost:5000/position/search",
        async:true,
        type:"GET",
        dataType:"json",
        success:function (result) {
            console.log(result);
            all_positions=result;
            result_positions=all_positions;
            indexPages();
        }
    })
}

//点击搜索
function searchPositions() {
     $('#btnSearch').on('click',function () {
         condition.search=$('#search').val().trim();
         if (condition.search){
             $.ajax({
                 url: "http://localhost:5000/position/searchposition",
                 async: true,
                 type: "GET",
                 data: {"search":condition.search},
                 dataType: "json",
                 success: function (result) {
                     console.log(result);
                     all_positions = result;
                     result_positions = all_positions;
                     condition.page_index=1;
                     getProfessions();
                     indexPages();
                 }
             })
         }
     })

}

//获取当前的result_positions
function getResult() {
    result_positions=[];
    for (let position of all_positions){
        if (condition.select_profession==position.profession_name){
            result_positions.push(position)
        }else if (condition.select_profession=='不限'){
            result_positions=all_positions
        }
    }
    indexPages()
}

//根据result_position分页
function indexPages() {
    //加载页码
    page_count=parseInt(result_positions.length/page_size)+1;
    loadPages(page_count);
    getPagePositions();
}

//确定当前页面需要的positions
function getPagePositions() {
    let start=(condition.page_index-1)*page_size;
    let end=condition.page_index*page_size-1;
    let positions=[];
    //页码是否大于length
    end=result_positions.length>end?end:result_positions.length-1;
    console.log(start,end);
    for (let i=start;i<=end;i++){
        positions.push(all_positions[i])
    }
    //渲染界面
    loadPostion(positions);
}

//渲染界面
function loadPostion(positions) {
    $('#job_main').html('');
    for (let position of positions){
        let time=format_date(position.publish_date);
        $('#job_main').append(`
             <div class="job-item" id="${position.id}">
                <div class="job-item-top">
                    <div class="job-item-top-left">
                        <span style="color: #00b38a">${position.name}【${position.city_name}】 ${time}</span> <br>
                        <span style="color: red">${position.salary}</span> 经验1-3年/ 本科
                    </div>
                    <div class="job-item-top-center">
                        <span style="color: #00b38a">${position.company_name}</span> <br>
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
        `)
    }
}
//加载页码
function loadPages(page_count) {
    $('#lin-page-index').empty();
    for (let i = 1; i <= page_count; i++) {
        $('#lin-page-index').append(`<a href="javascript:void 0">${i}</a>`)
    }
}

//给页码添加点击事件
function indexClick() {
    $('#lin-page-index').on('click','a',function () {
        condition.page_index=$(this).text();
        getPagePositions();
    })
}

//格式化时间
function format_date(str) {

    let date=new Date(str);

    let now=new Date();

    let days=parseInt(((now-date)/1000)/(24*60*60));
    if(days>3){
        return str.split(' ')[0];
    }else {
        return days+'天前发布'
    }

}