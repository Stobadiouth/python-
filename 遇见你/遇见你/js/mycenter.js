$(document).ready(function(){
    $('.div-table').click(function () {

       $('.div-table').css('background','rgba(182, 140, 186, 0.45)');
       $(this).css('background','white');
       $('.right').css('display','none');
       if ($(this).text()=='基本信息'){
           $('div.row>div.right')[0].style.display="block"
       }else if ($(this).text()=='详细信息') {
           $('div.row>div.right')[1].style.display="block"
       }else if ($(this).text()=='生活状况') {
           $('div.row>div.right')[2].style.display="block"
       }else if ($(this).text()=='兴趣爱好') {
           $('div.row>div.right')[3].style.display="block"
       }
   })
});