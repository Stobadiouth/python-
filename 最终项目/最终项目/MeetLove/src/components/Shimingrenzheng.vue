<template>
  <div class="container">
    <div class="row a">
      <h2>
        尊敬的用户，您提交的数据将会被加密处理，请放心填写~
      </h2>
    </div>
    <div class="row">
      <p class="col-md-2">真实姓名：</p>
      <input type="text" class="col-md-4" v-model="truename">
    </div>
    <div class="row">
      <p class="col-md-2">身份证：</p>
      <input type="text" class="col-md-4" v-model="peoplecode" style="margin-right: 20px">
      <p class="md" v-text="tishi01" :class="{red:tishi01=='身份证不符合条件'}" style="margin-top:10px;"></p>

    </div>
    <div class="row">
      <p class="col-md-2">手机号码：</p>
      <input type="text" class="col-md-4" v-model="tel">
      <button class="btn" v-show="sendAuthCode" @click="getAuthCode" :disabled="b==2">发送验证码</button><button v-show="!sendAuthCode" class="btn" ><span>{{auth_time}}</span> s 后无效</button>
    </div>
    <div class="row">
      <p class="col-md-2">验证码：</p>
      <input type="text" class="col-md-4" v-model="verification">
      <button class="btn"  @click="checkcode">进行认证</button>
      <div v-text="tishi04" style="color: red;font-size: 20px;font-weight: bolder;margin-left:500px;margin-top: 50px"></div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'Personal',
    data() {
      return {
        truename:'',
        uu:'',
        peoplecode:[],
        long:'',
        tel:'',
        tishi04:'',
        tishi01:'',
        b:2,
        sendAuthCode: true, /*布尔值，通过v-show控制显示‘获取按钮'还是‘倒计时' */
        auth_time:'', /*倒计时 计数器*/
        verification: "",//绑定输入验证码框框
        validate_code:"",//返回的验证码
      }
    },
    watch:{
      peoplecode:function(){
        let isIDCard1=/^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$/;
        //身份证正则表达式(18位)
        let isIDCard2=/^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$/;
        this.long=this.peoplecode.length;
        console.log(this.long==18);
        if (this.long==15){
          if (isIDCard1.test(this.peoplecode)) {

          }else {
            this.tishi01='身份证不符合条件'
          }
        }else if(this.long==18){
          if (isIDCard2.test(this.peoplecode)) {
            this.tishi01='身份证符合条件'
          }else {
            this.tishi01='身份证不符合条件'
          }
        }else {
          this.tishi01='身份证不符合条件'
        }
      },
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
            let params = new URLSearchParams();
            let id=localStorage.getItem('id');
            params.append('id', id);
            params.append('tel', this.tel);
            params.append('truename', this.truename);
            params.append('peoplecode', this.peoplecode);
            let vm=this;
            axios.post('http://47.106.14.132:8000/user/truename/',params)
              .then(function (response) {
                if (response.data['code']==202) {
                  vm.tishi04='认证成功！'
                }else {
                  vm.tishi04='已经实名认证过！'
                }
                let we= setInterval(() => {
                  vm.tishi04='';
                  vm.flag=false;
                }, 2000);
              });
          }else {
            this.tishi04='认证失败！';
            setTimeout(function () {
              vm.tishi04='';
            },2000)
          }
        }else {
          this.tishi04='认证失败！';
          setTimeout(function () {
            vm.tishi04='';
          },2000)
        }
      }
    }

  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .a{
    text-align: center;
    color:#FF6600;
    font-family: 华文琥珀;
    margin-top: 60px;
  }
  .row{
    margin-top: 50px}
  .col-md-2{
    margin-left:260px;
    padding-left:80px;
    font-size:18px;
    line-height: 40px;
    color: #A8A9A8;

  }
  input{
    height: 40px;
  }
  input:focus{
    outline: medium;
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
  .red{

    color: red;
  }


</style>
