<template>
  <form name="Hdxq" class="Hdxq">
  <div class="head">
    <h3>"告白气球"2018都市白领相亲大会</h3><br>
  </div>
  <div class="col-xs-6 col-md-1">
  </div>
  <div class="tp">
      <img src="../assets/hd2.jpg" height="500" width="700"/>

    <div class="tpxq">
      <p><img src="../assets/time.png" height="32" width="32"/>10月27日</p><br/>
      <p><img src="../assets/index.png" height="32" width="32"/>国际宴会中心</p><br/>
      <p><img src="../assets/regist.png" height="32" width="32"/>国际宴会中心</p><br/>
      <div class="btn-group-vertical" role="group" aria-label="...">


        <button type="button" class="alert alert-danger"  >
          活动微信二维码报名</button>
          <button><img src="../assets/erweima.jpg"></button>
        <p><img src="../assets/regist.png" height="20" width="20"/>已报名：54人</p><br/><br/>
        <p><router-link to="/regist"><button type="button" class=" alert alert-danger"style="text-align: center">我要关注</button></router-link></p><br/>
      </div>
    </div>
  </div>
  <div class="body">
    <div class="panel panel-default">
      <!-- Default panel contents -->
      <div class="alert alert-danger">活动提示</div>
      <div class="panel-body">
        <p>1、大胆的表现自己、不要拘束，加强别人对你的第一印象。 2、可带详细的证明材料，如照片、学历复印件等等，表示自己的诚信。 3、请听从工作人员安排，保持活动正常有序的进行。</p>
      </div>
      <div class="alert alert-danger">活动声明</div>
      <div class="panel-body">
        <p>1、请抱着严肃交友的态度来参加活动。 2、若您在中国红娘网有心仪网友，建议相邀在活动中见面，这是我们推荐的一种安全见面方式。 3、大胆联系朋友的同时请注意自己的隐私安全，谨慎择友。 4、活动参与人数以现场实际到达人数为准。 5、嘉宾必须对自己的一切行为负责，请确信您有足够的智慧和自我保护能力，不受侵害。</p>
      </div>
      <div class="direct">
        <div class="alert alert-danger">活动介绍</div>
        <div class="panel-body">
          <p>遇见爱网站以爱为名，用来帮助许多单身的帅哥美女们寻找自己的幸福，每当你自己一个人孤立无援时，遇见爱网站能够帮助你感受到不一样的温暖。</p><br/>
          <p>主办方设立服务咨询</p><br/>
          <p>会员和征婚者资料展示</p><br/>
          <p>现场设“幸福招亲点”</p><br/>
          <div class="photo">
            <img src="../assets/hdjs1.jpg"></div><br/>
        </div>
        <div class="photo">
          <img src="../assets/hdjs2.jpg" ><br/>
        </div>
      </div>
    </div>



    <div class="row2">
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">
        <strong>关于我们</strong><br>
        <router-link to='/about'><a href="#">关于我们</a></router-link>
        <router-link to='/about'><a href="#">关于我们</a><br></router-link>
        <router-link to='/about'><a href="#">关于我们</a></router-link>
        <router-link to='/about'><a href="#">关于我们</a><br></router-link>
        <router-link to='/about'><a href="#">关于我们</a></router-link>
        <router-link to='/about'><a href="#">关于我们</a><br></router-link>
      </div>
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">手机微信</div>

      <!-- Add the extra clearfix for only the required viewport -->
      <div class="clearfix visible-xs-block">
      </div>

      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">
        <strong>服务热线</strong><br>
        热线电话：0571-85337299
        <br>地址：杭州市朝晖路219号中山花园写字楼3楼 ( 地铁1号线西湖文化广场站，附近公交 车站：西湖文化广场，中北桥
      </div>
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">友情链接<br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br></div>
    </div>
      <div class="end">
        <p>版权所有</p>
        <p>遇见爱网 ◎版权所有 苏ICP备州B2-20090133</p>
      </div>

  </div>
  </form>
</template>

<script>
export default {
  name: "Hdxq",
    data() {
      return {
        b: "1"
    }
  },



}


</script>

<style scoped>
  .head{
    text-align: center;
  }
  .body{
    margin-top: 50px;
  }
  .head{
    color: #ff8899;
    text-shadow:2px 2px 2px rgba(143, 141, 134, 0.55);
  }
  .photo{
    text-align: center;
  }
  .end{
    color: grey;
    text-align: center;
    margin-top: 150px;
  }
  .tp{
    width: 700px;
    height: 500px;
    margin-left: 100px;
  }
  .tpxq{
    background: pink;
    height: 500px;
    width: 400px;
    margin-top: -500px;
    margin-left: 750px;
  }





</style>
