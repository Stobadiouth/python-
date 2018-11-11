<template>
  <div>
    <div class="row w">
      <div class="col-md-5 a">账号设置</div>
    </div>
    <div class="row ccc">
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==1}">
        <a href="#" @click="b=1" id="1" >个人设定</a>
      </div>
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==2}">
        <a href="#" @click="b=2" >修改密码</a>
      </div>
      <!--<div class="div-text col-md-2 col-sm-1" :class="{border:b==3}">-->
        <!--<a href="#" @click="b=3" >黑名单</a>-->
      <!--</div>-->

    </div>
    <div class="col-md-12">

      <div v-if="b==1">
        <div class="row bb">
          登录账号： <span v-text="zhang"></span>
        </div>
        <div class="row bb">
          恋爱状态：
          <input type="radio" id="xunmi" checked="checked" name="sport" value="nba">
          <label name="nba" :class="{checked:g=='寻觅中'}" @click="g='寻觅中'" for="xunmi">寻觅中</label>
          <input type="radio" id="yuehui" name="sport" value="cba">
          <label name="cba" for="yuehui" :class="{checked:g=='约会中'}" @click="g='约会中'">约会中</label>
          <input type="radio" id="lianai" name="sport" value="cba">
          <label name="cba" for="lianai" :class="{checked:g=='恋爱中'}" @click="g='恋爱中'">恋爱中</label>
        </div>
        <div class="row bb cc">
          资料设置：
          <input type="radio" id="baihe" checked="checked" name="sport" value="nba">
          <label name="nba" :class="{checked:k=='百合用户可见'}" @click="k='百合用户可见'" for="baihe">百合用户可见</label>
          <input type="radio" id="yincang" name="sport" value="cba">
          <label name="cba" for="yincang" :class="{checked:k=='隐藏资料'}" @click="k='隐藏资料'">隐藏资料</label>
          <input type="radio" id="shiming" name="sport" value="cba">
          <label name="cba" for="shiming" :class="{checked:k=='仅好友可见'}" @click="k='仅好友可见'">仅好友可见</label>
        </div>
        <div class="row bb">
          只限通过实名认证的用户查看：
          <input type="radio" id="shi" checked="checked" name="sport" value="nba">
          <label name="nba" :class="{checked:m=='是'}" @click="m='是'" for="shi">是</label>
          <input type="radio" id="fou" name="sport" value="cba">
          <label name="cba" for="fou" :class="{checked:m=='否'}" @click="m='否'">否</label>
        </div>
        <div v-text="tishi05" style="color: red;font-size: 20px;font-weight: bolder;margin-left: 380px;padding-top:100px"></div>
        <button class="btn" @click="change">保存</button>
      </div>
      <div v-else-if="b==2">
        <div class="row yan ">
        <p class="col-md-2">当前密码：</p>
        <input type="password" class="col-md-4" v-model="oldpassword" placeholder="请在这里输入原密码" @blur="oldsure">
        <p class="md" v-text="tishi01" :class="{black:tishi01=='密码正确'}"></p>
      </div>
        <div class="row yan ">
          <p class="col-md-2">新密码：</p>
          <input type="password" class="col-md-4" v-model="newpassword" placeholder="请输入6-16位英文字母或数字。" @blur="newsure">
          <p class="md" v-text="tishi02" :class="{black:tishi02=='新密码格式正确！'}"></p>
        </div>
        <div class="row yan ">
          <p class="col-md-2">确认新密码：</p>
          <input type="password" class="col-md-4" v-model="newpassword01" placeholder="请确认新密码。" @blur="newsure01">
          <p class="md" v-text="tishi03" :class="{black:tishi03=='密码正确！'}"></p>
        </div>
        <div v-text="tishi04" style="color: red;font-size: 20px;font-weight: bolder;margin-left: 380px;padding-top:100px"></div>
        <button class="btn" @click="changepassword">保存</button>

      </div>
    </div>
  </div>

</template>

<script>
  import axios from 'axios';
  import $ from 'jquery'
  export default {
    name: 'Ziliaojindu',
    data() {
      return {
        oldpassword:'',
        newpassword:'',
        newpassword01:'',
        tishi01:'',
        tishi02:'',
        tishi03:'',
        tishi04:'',
        tishi05:'',
        makesure:0,
        zhang:'877476153',
        mima:'',
        c:"1",
        b: "1",
        g:"寻觅中",
        k:"百合用户可见",
        m:"是"
      }
    },
    mounted: function () {
      this.zhanghao()
    },
    methods: {
      zhanghao:function(){
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/getmes/',params)
          .then(function (response) {
            let s0=response.data;
            vm.zhang=s0['tel'];
            vm.mima=s0['password'];
            if (s0['love']) {
              vm.g=s0['love']
            }
            if (s0['check']) {
              vm.k=s0['check']
            }
            if (s0['ifsee']) {
              vm.m=s0['ifsee']
            }
          });
      },
      change:function () {
        let u={
          'id':localStorage.getItem('id'),
          'love':this.g,
          'check':this.k,
          'ifsee':this.m
        };
        let vm=this;
        $.ajax(
          {
            url:'http://47.106.14.132:8000/user/baocunmes/',
            type:"POST",
            data:JSON.stringify(u),
            dataType:"json",
            contentType:"application/json",
            success:function (response,textStatus,xhr) {
              vm.tishi05='修改成功！';
              setTimeout(function () {
                vm.tishi05=''
              },2000)

            },
            error:function (XMLHttpRequest,textStatus,errorThrown) {
              vm.tishi05='修改失败！';
              setTimeout(function () {
                vm.tishi05=''
              },2000)
            }
          }
        )
      },
      oldsure:function () {
        if (this.oldpassword==this.mima){
          this.tishi01='密码正确'
        }else{
          this.tishi01='密码错误'
        }
      },
      newsure:function () {
        let reg=/^\w{6,16}$/;
        if (this.newpassword==''){
          this.tishi02='密码不能为空！'
        } else if (this.newpassword.length<6) {
          this.tishi02='密码长度小于6！'
        }else if (this.newpassword.length>16) {
          this.tishi02='密码长度大于16！'
        }else if (reg.test(this.newpassword)) {
          this.tishi02='新密码格式正确！'
        }else{
          this.tishi02='请输入6-16位英文字母或数字。'
        }
      },
      newsure01:function () {
        if (this.newpassword01!='' & this.newpassword01==this.newpassword){
          this.tishi03='密码正确！';
          this.makesure=1
        }else if(this.newpassword01==''){
          this.tishi03='密码不能为空！'
        }
        else {
          this.tishi03='两次密码不一样！'
        }
      },
      changepassword:function () {
        if (this.makesure==1) {
          let params = new URLSearchParams();
          let id=localStorage.getItem('id');
          let vm=this;
          params.append('id', id);
          params.append('password', this.newpassword01);
          axios.post('http://47.106.14.132:8000/user/changepassword/',params)
            .then(function (response) {
              if (response.data["code"]==202) {
                vm.tishi04='密码更改成功！';
                setTimeout(function () {
                  vm.tishi04='';
                  vm.makesure=0
                },2000)
              }else {
                vm.tishi04='密码更改失败！';
                setTimeout(function () {
                  vm.tishi04=''
                },2000)
              }

            });
        }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  a {
    text-decoration: none;
    font-size: 16px;
  }

  a:link {
    color: black;
  }
  a:visited {
    color: black;
  }
  a:hover {
    text-decoration: none;
    color: orangered;
  }
  .ccc {
    border-bottom: solid red 1px;
  }
  .div-text:hover{
    border-bottom: solid 3px #F23A6E;
  }
  .div-text {
    height: 100%;
    line-height: 55px;
    margin-left: 10px;
    text-align: center;
  }
  .border {
    height: 100%;
    text-align: center;
    line-height: 55px;
    border-bottom: solid 3px #F23A6E;
  }
  .a{
    height: 30px;
    font-size:25px;
  }
  .b span{
    color: #FF6600;
    font-size:20px;
  }
  .col-md-2{
    padding: 0;
    padding-left:15px;
  }
  .w{
    padding-top: 20px;
    line-height: 16px;
  }
  .bb{
    color: rgba(0, 0, 0, 0.66);
    font-size:16px;
    margin-left: 10px;
    margin-top:20px;
  }
  .bb span{
    color: #BDBDBD;
    font-size: 14px;
  }



  input[type="radio"] {
    display: none;
  }
  label {
    font-size: 16px;
    line-height:18px;
    padding-left: 20px;
    cursor: pointer;
    background: url(../assets/personal/按钮.png) no-repeat left top;
  }
  label.checked {
    background: url(../assets/personal/按钮颜色.png) no-repeat left top;
  }
.cc label{
  display: block;
  margin-top: 20px;
  margin-left: 20px;
  font-family: "微软雅黑 Light";
}
  .btn {
    width: 80px;
    height: 50px;
    background: rgba(180, 3, 3, 0.8);
    color: white;
    margin-left: 400px;
    margin-top: 50px;
  }



  .yan{
    margin-top:30px;
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
    margin-right: 20px;
  }
  .md{
    color: red;
    line-height: 40px;

  }
  .black{
    color: #0e0e0e;
  }
.im{
  margin-top:80px;
  margin-left:120px;
  font-family: "微软雅黑", "黑体";
  font-size: 18px;
}
.ziti{
  margin-top:40px;
  font-size:16px;
  color:#A8A9A8 ;
}









</style>
