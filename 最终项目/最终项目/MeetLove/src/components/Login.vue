<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-2"></div>
      <div class="col-md-4">
        <div class="login row">
          <div class="logo"><img src="../assets/index/love.png" alt=""></div>
          <div class="div-input row">
            <div class="col-md-3">账号：</div>
            <div class="col-md-8">
              <input class="form-control" type="text" placeholder="请输入账号" id="telephone" v-model="tel" @input="check_tel">
              <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true" v-if="sign===true"></span>
              <span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true" v-else-if="sign===false"></span>
            </div>
          </div>
          <div class="div-input row">
            <div class="col-md-3">密码：</div>
            <div class="col-md-8">
              <input class="form-control" type="password" placeholder="请输入密码" id="password" v-model="password" @input="check_pwd">
              <span class="glyphicon glyphicon-ok form-control-feedback" aria-hidden="true" v-if="flag===true"></span>
              <span class="glyphicon glyphicon-remove form-control-feedback" aria-hidden="true" v-else-if="flag===false"></span>
            </div>
          </div>
          <p v-show="error" id="error">用户名或密码错误</p>
          <div class="row div-check">
            <div class="col-md-4">
              <label class="checkbox-inline">
                <input type="checkbox" id="" value="option1" v-model="checked"> 记住密码
              </label>
            </div>
            <div class="col-md-8"><a href="" class="text-danger">忘记密码？</a></div>
          </div>
          <div>
            <button class="btn" @click="login_in">立即登录</button>
          </div>
          <div>
            <router-link to="/register"><button class="btn regist">免费注册</button></router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import $cookie from 'vue-cookie'
  import $ from 'jquery'
export default {
  name: 'Login',
  data () {
    return {
      tel:'',
      password:'',
      sign:null,
      flag:null,
      error:false,
      checked:false
  }
  },
  methods:{
    check_tel:function () {
      let reg=/^\d{11}$/;
      if (reg.test(this.tel)) {
        this.sign=true
      }else {
        this.sign=false
      }
    },
    check_pwd:function () {
      let reg=/^\w{6,16}$/;
      if (reg.test(this.password)) {
        this.flag=true
      }else {
        this.flag=false
      }
    },
  //  登录
    login_in:function () {
      let _this=this;
      if (this.sign && this.flag){
        $.ajax({
          url:'http://47.106.14.132:8000/user/login/',
          type:"POST",
          data:JSON.stringify({"tel":this.tel,"password":this.password}),
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
              //记住用户名和密码
              _this.Save()
              _this.$router.push({path:'/'})
            }else {
              _this.error=true
              console.log(_this.error)
            }
          },
          error:function (XMLHttpRequest,textStatus,errorThrown) {
            console.log('nononon');
            console.log(textStatus)
          }
        })
      }
    },
    //记住用户名密码
    Save:function () {
      if (this.checked) {
        //设置一个小时的cookie
        let now = new Date();
        now.setTime(now.getTime() + 60* 60 * 1000);
        $cookie.set("rmbUser", "true", { expires: now }); //存储一个带7天期限的cookie
        $cookie.set("telephone", this.tel, { expires: now });
        $cookie.set("password", this.password, { expires: now });
      }
      else {
        $cookie.set("rmbUser", "false", { expire: -1 });
        $cookie.set("telephone", "", { expires: -1 });
        $cookie.set("password", "", { expires: -1 });
      }
    }
  },
  mounted:function () {
    if ($cookie.get('rmbUser')){
      this.checked=true;
      this.tel=$cookie.get('telephone');
      this.password=$cookie.get('password');
      this.sign=true;
      this.flag=true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body,ul,li,p,a,div,h2,h3,span,hr,button{
    margin: 0;
    padding:0;
  }
  .container-fluid{
    padding: 0!important;
    width: 100%;
    height: 700px;
    background: url("../assets/login_regist_images/bj.jpg");
    background-size: cover;
  }

  .login{
    width: 430px;
    height: 500px;
    border-radius: 4px;
    margin-top: 140px;
    background: rgba(91, 91, 91, 0.54);
    box-shadow: 0 2px 11px 0 rgba(0,0,0,0.5);
    text-align: center;
    font-size: 1.2em;
  }
  .logo{
    margin-top: 20px;
    padding-bottom: 20px;
    border-bottom: 2px solid #d4d4d4;
  }
  .logo img{
    width: 130px;
    height: 50px;
  }
  .div-input>div{
    margin-top: 30px;
    height: 40px;
    text-align: left;
    padding: 0;
  }
  .div-input>div:nth-of-type(1){
    line-height: 30px;
    padding-left: 50px;
  }

  .div-check{
    margin-top: 40px;
    padding: 0;
  }

  .div-check>div:nth-of-type(1){
    padding-left: 50px;
  }
  .div-check a{
    margin-left: 130px;
    text-decoration: none!important;
  }


  .btn{
    width: 320px;
    height: 40px;
    border-radius: 4px;
    background-color: #595B6A;
    font-size: large!important;
    margin-top: 30px;
    color: lightblue;
    box-shadow: 2px 2px 2px 2px grey;
  }
  .regist{
    margin-top: 20px;
    background: rgba(192, 231, 245, 0.98);
    color: #6a6a6a;
  }
  #error{
    margin-top: 10px;
    font-size: small;
    color: rgba(211, 0, 0, 0.9);
  }
</style>
