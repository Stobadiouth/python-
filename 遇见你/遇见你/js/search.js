window.onload=function () {
    //给排序方式添加点击事件
    document.querySelector('.search-second').onclick=function (e) {
        event=e.target;
        if(event.tagName=='SPAN'){
            let sp=this.querySelectorAll('span');
            for (let i of sp){
                i.style.background=' rgba(173, 173, 173, 0)'
            }
            event.style.background=' rgba(255, 182, 193, 0.76)'
        }
    }
}