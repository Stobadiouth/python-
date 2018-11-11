<template>
  <div class="head">
    <div class="jumbotron">
        <h1 class="timu" style="color: white">关于我们</h1>
        <p class="ftimu" style="color: white"> Cooperative Partner</p>
        <p class="ftimu" ><img src="../assets/heart .png" height="32" width="32"/> </p>
    </div>
    <div class="media"style="background:#fffcfb">
      <div class="media-left">
        <a href="#">
          <img class="media-object" src="../assets/爱心 (1).png" alt="...">
        </a>
      </div>
        <div class="media-body">
          <h4 class="media-heading">企业介绍</h4>
          遇见爱(www.HongNiang.com)是苏州都市家庭旗下品牌。网站拥有各类注册会员近1000万，VIP会员超100万。截至2018年，共举办大小活动1500余场，已有数十万单身男女通过遇见爱网找到了自己的幸福.
        </div>

    </div>
    <div class="media"style="background:#fffcfb">
      <div class="media-left">
        <a href="#">
          <img class="media-object" src="../assets/爱心 (1).png" alt="...">
        </a>
      </div>

      <div class="media-body">
        <h4 class="media-heading">品牌历程</h4>
        <h5>2018 5月 :确立项目，命名为遇见爱。</h5>
        <h5>2018 9月 :正式确立项目，整个风格以清新简洁为主，凸显现代社会的时尚活力。</h5>
        <h5>2018 10月 :进入项目收尾阶段，网站即将启动</h5>
        <h5>2018 10月 :遇见爱正式确立</h5>
      </div>

    </div>
    <div class="media"style="background:#fffcfb">
      <div class="media-left">
        <a href="#">
          <img class="media-object" src="../assets/爱心 (1).png" alt="...">
        </a>
      </div>
      <div class="media-body">
        <h4 class="media-heading">网站功能</h4>
        <h5>用户：用户自身管理，会员信息展示，网站信息展示，用户留言以及用户之间的相互交流</h5>
        <h5>管理员：自身管理，用户管理，活动管理，留言处理</h5>
        <h5>查找：可以根据自己的条件进行筛选，最终选出自己心仪的对象</h5>
        <h5>安全：本网站有律师咨询顾问等功能，当自己的安全和财产受到侵害时，可通过律师咨询进行维权</h5>
      </div>
    </div>
    <div class="page-header">
      <h1 class="connect">联系我们</h1>
    </div>
    <div class="row">
      <div class="col-xs-6 col-md-3">
      </div>
      <div class="col-xs-6 col-md-4">
        <a href="#" class="thumbnail">
          <img src="../assets/map.png" >
        </a>
      </div>
      <div class="col-xs-6 col-md-3">
        <p>遇见爱网址www.yja.com 总部：</p>
        <p>0571-87756577、18768136650 </p><br>
        <p>0571-87756575、15168217182 </p><br>
        <p>功能：渠道合作、活动策划等 </p><br><br>
        <p>0571-89715001 </p><br>
        <p>遇见爱网址www.yja.com 总部：</p>
        <p>0571-87756577、18768136650 </p><br>
        <p>0571-87756575、15168217182 </p><br>
      </div>
      <div class="col-xs-6 col-md-2">
      </div>
    </div>
    <div class="row">
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">
        <strong>关于我们</strong><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
      </div>
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">手机微信</div>

      <!-- Add the extra clearfix for only the required viewport -->
      <div class="clearfix visible-xs-block">
      </div>

      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">
        <strong>服务热线</strong><br>
        热线电话：0571-85337299
        <br>地址：杭州市朝晖路219号中山花园写字楼3楼 ( 地铁1号线西湖文化广场站，附近公交 车站：西湖文化广场，中北桥</br>
        </address></div>
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">友情链接<br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br></div>
    </div>
  </div>





</template>

<script>
    export default {
        name: "About",
        data() {
          return {
            b: "1"
          }
        },
    }
</script>

<style scoped>
.jumbotron{
  background: pink;
}
  .timu{
    text-align: center ;
  }
  .ftimu{
    text-align: center ;
    padding-top: 10px;
  }
  .media-body{
    color: rgba(82, 82, 82, 0.94);
  }

  .connect{
    text-align: center;
    color: grey;
  }


</style>
