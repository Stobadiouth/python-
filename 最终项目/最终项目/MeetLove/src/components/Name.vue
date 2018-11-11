<template>
  <div>
    <div class="row b">
      <div class="col-md-5 a">实名认证</div>
    </div>
    <div class="row">
      <div class="col-md-2 c">
        <img src="../assets/personal/实名认证大.png" alt="">
      </div>
      <div class="col-md-8 d">
        实名认证可有效预防身份信息被冒用风险。认证通过后，<br/>
        点亮 <img src="../assets/personal/实名认证颜色.png" alt="实名"/> 徽章。<br/>
        <p class="orangeT">所有用户均可免费认证。</p>

      </div>
    </div>
      <div class="row e">
        <router-link to="/shimingrenzheng"><a href="#" class="orange">开始认证</a></router-link>
      </div>
    <div class="authInfo row">
      <h5>认证小贴士：</h5>
      <ul>
        <li><em>1</em><div class="txt">点亮 <img src="../assets/personal/实名认证颜色.png" alt="实名" /> 标示，增强征友效果，受到更多关注和推荐；</div></li>
        <li><em>2</em><div class="txt">有权查看设置了“通过认证的会员可见”会员的照片及资料；</div></li>
        <li><em>3</em><div class="txt">遇见爱努力打造贴心、安全的婚恋交友环境，实名认证的会员可信度高；</div></li>
        <li><em>4</em><div class="txt">每个身份证只能绑定一个账号。</div></li>
      </ul>
    </div>
  </div>

</template>

<script>
  export default {
    name: 'Name',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .a {
    height: 30px;
    font-size: 25px;
  }

  .b {
    padding-top: 20px;
    line-height: 16px;
  }

  .c {
    margin-top: 50px;
    margin-left: 50px;
  }

  .d {
    margin-top: 60px;
    color: #666666;
    font-size: 17px;
  }

  .orangeT {
    color: #FF6600;
  }
  .e{
    display: block;
    width: 150px;
    height:40px;
    font-size: 15px;
    background: #ff8d19;
    text-align: center;
    line-height: 40px;
    border-radius:5px;
    margin-top: 50px;
    margin-left: 500px;
  }
  .e:hover{
    background: #FF6600;
  }
  a{
    color: #FFFFFF;
    text-decoration: none;
  }

  .authInfo {margin-top: 30px; padding:15px 40px; font-size:13px; background:#fafdff; border:1px solid #ebeef0; overflow:hidden; zoom:1; }
  .authInfo h5 { height:30px; font-size:16px;}
  .authInfo ul li { padding-bottom:5px; overflow:hidden; zoom:1; }
  .authInfo em { display:block; float:left; width:18px; height:18px; margin-top:5px; font-size:13px; line-height:17px; color:#fff; text-align:center; background:url(http://images9.baihe.com/auth/zmrz_arrow.gif) no-repeat; overflow:hidden; zoom:1; }
  .authInfo .txt { float:left; width:700px; padding-left:7px; font-size:13px; line-height:26px; overflow:hidden; zoom:1; }
  .authInfo p { line-height:26px;}
</style>
