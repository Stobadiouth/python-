<template>
  <div>
    <div class="row b">
      <div class="col-md-5 a">手机认证</div>
    </div>
    <div class="row">
      <div class="col-md-2 c">
        <img src="../assets/personal/手机充值大.png" alt="">
      </div>
      <div class="col-md-8 d">
        请填写手机号码通过手机认证，通过认证后点亮<img src="../assets/personal/手机充值颜色.png" alt="实名"/> 徽章。<br/>
        <p class="orangeT">所有用户均可免费认证。</p>
      </div>
    </div>
    <div class="row yan " :class="{t:flag}">
      <p class="col-md-2">手机号：</p>
      <input type="text" class="col-md-4" v-model="tel">
      <button class="btn" v-show="sendAuthCode" @click="getAuthCode" :disabled="b==2">发送验证码</button>
      <button v-show="!sendAuthCode" class="btn" ><span>{{auth_time}}</span> s 后无效</button>

    </div>
    <div class="row yan " :class="{t:flag}" >
      <p class="col-md-2">验证码：</p>
      <input type="text" class="col-md-4" v-model="verification">
      <button class="btn" @click="checkcode">提交验证码</button>
      <div v-text="tishi04" style="color: red;font-size: 20px;font-weight: bolder;margin-left: 380px;margin-top: 50px"></div>

    </div>
    <div class="row e" :class="{tt:flag} ">
      <a href="#" class="orange" @click.stop.prevent="chan">更改手机</a>
    </div>
    <div class="authInfo row">
      <h5>认证小贴士：</h5>
      <ul>
        <li><em>1</em><div class="txt">点亮 <img src="../assets/personal/手机充值颜色.png" alt="实名" /> 标示，提升个人形象，增强征友效果；</div></li>
        <li><em>2</em><div class="txt">有权查看设置了“通过认证的会员可见”会员的照片及资料；</div></li>
        <li><em>3</em><div class="txt">遇见爱努力打造贴心、安全的婚恋交友环境，认证的会员将获得更多关注和推荐；</div></li>
        <li><em>4</em><div class="txt">每个手机号码只能绑定一个账号。</div></li>
      </ul>
    </div>
  </div>

</template>

<script>
  import axios from 'axios';
  export default {
    name: 'Phone',
    data() {
      return {
        tishi04:'',
        b:2,
        tel:'',
        sendAuthCode: true, /*布尔值，通过v-show控制显示‘获取按钮'还是‘倒计时' */
        auth_time:'', /*倒计时 计数器*/
        verification: "",//绑定输入验证码框框
        validate_code:"",//返回的验证码
        flag: false,
      }
    },
    watch:{
      tel:function () {
        let reg=/^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\d{8}$/;
        if (reg.test(this.tel)) {
          this.b=1
        }else{
          this.b=2
        }
      }
    },
    methods:{
      chan:function () {
        this.flag=true;
      },
      getAuthCode: function () {
        let params = new URLSearchParams();
        params.append('tel',this.tel);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/getmobilecode/',params)
          .then(function (response) {
            console.log(response.data['validate_code']);
            vm.validate_code=response.data['validate_code'];
          });
        this.sendAuthCode = false;
        //设置倒计时秒
        this.auth_time = 60;
        var auth_timetimer = setInterval(() => {
          this.auth_time--;
          if (this.auth_time <= 0) {
            this.sendAuthCode = true;
            clearInterval(auth_timetimer);
          }
        }, 1000);
      },
      checkcode:function () {
        let vm=this;
        if (this.auth_time) {
          if (this.verification==this.validate_code) {
            this.tishi04='更改成功！';
            let params = new URLSearchParams();
            let id=localStorage.getItem('id');
            params.append('id', id);
            params.append('tel', this.tel);
            let vm=this;
            axios.post('http://47.106.14.132:8000/user/savetel/',params);
            let we= setInterval(() => {
              vm.tishi04='';
              vm.flag=false;
            }, 2000);

          }else {
            this.tishi04='更改失败！';
            setTimeout(function () {
              vm.tishi04='';
            },2000)
          }
        }else {
          this.tishi04='更改失败！';
          setTimeout(function () {
            vm.tishi04='';
          },2000)
        }
      }

    },

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

  .authInfo {
    margin-top: 30px;
    padding:15px 40px;
    font-size:13px;
    background:#fafdff;
    border:1px solid #ebeef0;
    overflow:hidden; zoom:1;
  }
  .authInfo h5 { height:30px; font-size:16px;}
  .authInfo ul li { padding-bottom:5px; overflow:hidden; zoom:1; }
  .authInfo em { display:block; float:left; width:18px; height:18px; margin-top:5px; font-size:13px; line-height:17px; color:#fff; text-align:center; background:url(http://images9.baihe.com/auth/zmrz_arrow.gif) no-repeat; overflow:hidden; zoom:1; }
  .authInfo .txt { float:left; width:700px; padding-left:7px; font-size:13px; line-height:26px; overflow:hidden; zoom:1; }
  .authInfo p { line-height:26px;}
  .yan{
    margin-top:30px;
    display: none;
  }
  .yan .col-md-2{
    margin-left: 100px;
    padding-left: 50px;
    font-size: 18px;
    color:  #A8A9A8;
    line-height: 40px;
  }
  .yan input{
    height:40px;
  }
  .btn{
    margin-left: 10px;
    width:100px;
    height: 40px;
    background:#ff8d19;
  }
  .btn:hover{
    background:  #FF6600;
  }
  .t{
    display: block;
  }
  .tt{
    display: none;
  }

</style>
