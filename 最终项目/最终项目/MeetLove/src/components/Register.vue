<template>
  <div class="container-fluid">
    <div class="regist">
      <div class="title">还等什么呢？抓紧谈恋爱吧！</div>
      <div class="title-tips">别忘了一定要填写真实信息哦</div>
      <div class="row sex">
        <div class="col-md-2">性别</div>
        <div class="col-md-1"></div>
        <div class="col-md-8">
          <label class="radio-inline">
            <input type="radio" name="inlineRadioOptions" id="inlineRadio1" value="1" v-model="picked"><img src="../assets/login_regist_images/男.png">
          </label>
          <label class="radio-inline">
            <input type="radio" name="inlineRadioOptions" id="inlineRadio2" value="0" v-model="picked"><img src="../assets/login_regist_images/女.png" >
          </label>
        </div>
      </div>
      <div class="row regist-input">
        <div class="col-md-2">手机号</div>
        <div class="col-md-8">
          <input type="text" class="form-control" id="telephone" placeholder="请输入手机号" v-model="tel" @input="check_tel">
          <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true" v-if="tel_flag===true"></span>
          <span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true" v-else-if="tel_flag===false"></span>
        </div>
      </div>
      <div class="row regist-input">
        <div class="col-md-2">验证码</div>
        <div class="col-md-5">
          <input type="text" class="form-control" id="yzm" placeholder="输入验证码" v-model="yzm">
        </div>
        <div class="col-md-3" id="imgsure" @click="refreshCode">
          <identify :identifyCode="identifyCode"></identify>
        </div>
      </div>
      <div class="row regist-input">
        <div class="col-md-2">密码</div>
        <div class="col-md-8">
          <input type="password" class="form-control" id="password" placeholder="请输入密码" v-model="password1" @input="check_pwd">
          <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true" v-if="pwd1_flag===true"></span>
          <span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true" v-else-if="pwd1_flag===false"></span>
        </div>
      </div>
      <div class="row regist-input">
        <div class="col-md-2">确认密码</div>
        <div class="col-md-8">
          <input type="password" class="form-control" id="password2" placeholder="请确认密码" v-model="password2">
          <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true" v-if="password1===password2"></span>
          <span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true" v-else></span>
        </div>
      </div>
      <div id="error" v-show="error">用户已经被注册过了</div>
      <div class="row div-btn">
        <button class="btn" @click="regist">免费注册</button>
      </div>
    </div>
  </div>
</template>

<script>
  import $ from 'jquery'
export default {
  name: 'Register',
  data () {
    return {
      tel:'',
      password1:'',
      password2:'',
      tel_flag:null,
      pwd1_flag:null,
      identifyCodes: "1234567890",
      identifyCode: "",
      yzm:'',
      picked:1,
      error:false
    }
  },
  mounted() {
    this.identifyCode = "";
    this.makeCode(this.identifyCodes, 4);
  },
  methods: {
    //获取验证码
    randomNum(min, max) {
      return Math.floor(Math.random() * (max - min) + min);
    },
    refreshCode() {
      this.identifyCode = "";
      this.makeCode(this.identifyCodes, 4);
    },
    makeCode(o, l) {
      for (let i = 0; i < l; i++) {
        this.identifyCode += this.identifyCodes[
          this.randomNum(0, this.identifyCodes.length)
          ];
      }
      console.log(this.identifyCode);
    },

    check_tel: function () {
      let reg = /^\d{11}$/;
      if (reg.test(this.tel)) {
        this.tel_flag = true
      } else {
        this.tel_flag = false
      }
    },
    check_pwd: function () {
      let reg = /^\w{6,16}$/;
      if (reg.test(this.password1)) {
        this.pwd1_flag = true
      } else {
        this.pwd1_flag = false
      }
    },
    regist:function () {
      let _this=this;
      if (this.tel_flag && this.pwd1_flag && this.password1===this.password2 && this.identifyCode===this.yzm){
        let user={
          "tel":this.tel,
          "password":this.password1,
          "sex_id":this.picked
        };
        console.log(user);
        $.ajax({
          url:'http://47.106.14.132:8000/user/regist/',
          type:"POST",
          data:JSON.stringify(user),
          dataType:"json",
          contentType:"application/json",
          success:function (response,textStatus,xhr) {

            console.log(response);
            console.log(textStatus);
            // console.log(request.getAllResponseHeaders())
            console.log(xhr.getResponseHeader('token'));
            if (response['id']){
              localStorage.setItem('id',response['id']);
              localStorage.setItem('token',xhr.getResponseHeader('token'));
              _this.$router.push({path:'/'})
            }
            else {
              _this.error=true
            }
          },
          error:function (XMLHttpRequest,textStatus,errorThrown) {
            console.log('nononon');
            console.log(textStatus)
          }
        })
      }else {
        this.refreshCode()
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body,ul,li,p,a,div,h2,h3,span,hr{
    margin: 0;
    padding:0;
  }
  .container-fluid{
    background:url("../assets/login_regist_images/001.png") ;
    height: 700px;
    padding: 0;
  }


  .regist{
    margin-top: 50px;
    margin-left: 500px;
    width: 600px;
    border-radius: 2px;
    background-color: rgba(122, 85, 74, 0.31);
    box-shadow: 0 0 6px 0 #f1f1f1;
    height: 550px;
  }

  .title{
    font-weight: bold;
    font: 18px/53px 'Microsoft Yahei';
    color:#f3316b;
    text-align: center;
  }
  .title-tips {
    color: #3c3c3c;
    height: 37px;
    line-height: 37px;
    background-color: rgba(112, 126, 119, 0.44);
    text-align: center;
    margin-bottom: 40px;
  }

  .sex{
    margin-top: 20px;
    font-size: 18px;
    padding-left: 80px;
  }

  .regist-input{
    margin-top: 20px;
    font-size: 18px;
    padding-left: 80px;
  }
  .regist-input input{
    background-color: rgba(112, 126, 119, 0.44);
    margin-left: 20px;
  }

  #imgsure{
    /*height: 30px;*/
    margin-left: 30px;
  }

  .div-btn{
    margin-top: 30px;
    text-align: center;
  }
  .btn{
    width: 350px;
    background-color:#845779;
    color: black;
    font-size: 18px!important;
  }
  #error{
    margin-top: 10px;
    font-size: small;
    color: rgba(211, 0, 0, 0.9);
    text-align: center;
  }
</style>
