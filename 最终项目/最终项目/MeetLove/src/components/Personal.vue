<template>
  <div class="container">
    <div class="row">
      <div class="col-md-12 a">
        <div class="row">
          <div class="col-md-2 col-sm-2 col-xs-3 p">
            <img :src="picture" alt="..." class=" img-circle img-responsive touxiang" style="width: 130px;height: 130px">
          </div>
          <ul class="col-md-7 col-sm-7 col-xs-9 q">
            <li>
              <div class="name" v-text="name0">www</div>
              <div>我的等级：<span v-text="huiyuan"></span></div>
              <div class="per-img" style="cursor: pointer">等级认证：<img :src="phone" alt="a1" @click="b=4"><img :src="name" alt="a2" @click="b=3"><img :src="yi" alt="a3" @click="b=5"><img :src="message" alt="a4" @click="b=1"></div>
              <div style="cursor: pointer">财富值：<img src="../assets/personal/钱.png" alt="" @click="b=9"></div>
            </li>
            <li class="massage">
              <div>安全提示：加强自我防范意识，警惕投资、理财、赌彩等诈骗方式!</div>
              <div>
                <ul class="massage01">
                  <li>
                    <ul  class="massage03">
                      <li v-text="xiaoxi"></li>
                      <li class="massage02"><router-link to="/email"><a href="#">未读消息</a></router-link></li>
                    </ul>
                  </li>
                  <li>
                    <ul  class="massage03">
                      <li v-text="t"></li>
                      <li class="massage02" @click="b=8" ><a href="#">最近访问量</a></li>
                    </ul>
                  </li>
                  <li>
                    <ul class="massage03">
                      <li v-text="jinbi"></li>
                      <li class="massage02" @click="b=9" ><a href="#">我的金币</a></li>
                    </ul>
                  </li>
                  <li>
                    <ul class="massage03">
                      <li v-text="jifen"></li>
                      <li class="massage02" @click="b=10" ><a href="#">我的积分</a></li>
                    </ul>
                  </li>
                </ul>
              </div>
            </li>
          </ul>
          <div class="col-md-3 col-sm-3">
            <img src="../assets/personal/advert.jpg" alt="" class="img-responsive ">
          </div>
        </div>
      </div>
    </div>
    <div class="row m" >
      <div class="row ">
        <ul class="nav nav-pills nav-stacked col-md-2">
          <li role="presentation" @click="b=1" :class="{active:1===b}"><a href="#" class="h">我的资料</a></li>
          <li role="presentation" @click="b=2" :class="{active:2===b}"><a href="#" class="h">我的会员</a></li>
          <li role="presentation" @click="b=3" :class="{active:3===b}"><a href="#" class="h">实名认证</a></li>
          <li role="presentation" @click="b=4" :class="{active:4===b}"><a href="#" class="h">手机认证</a></li>
          <li role="presentation" @click="b=5" :class="{active:5===b}"><a href="#" class="h">择偶意向</a></li>
          <li role="presentation" @click="b=6" :class="{active:6===b}"><a href="#" class="h">账号设置</a></li>
          <li role="presentation" @click="b=7" :class="{active:7===b}"><a href="#" class="h">我的活动</a></li>
        </ul>
        <div class="col-md-10">

          <div v-if="b==1">
            <material @pic04="pic05" @namechange04="namechange05"></material>
          </div>
          <div v-else-if="b==2">
            <vip></vip>
          </div>
          <div v-else-if="b==3">
            <name></name>
          </div>
          <div v-else-if="b==4">
            <phone></phone>
          </div>
          <div v-else-if="b==5">
            <friend></friend>
          </div>
          <div v-else-if="b==6">
            <root></root>
          </div>
          <div v-else-if="b==7">
            <myactive></myactive>
          </div>
          <div v-else-if="b==8">
            <seeme @memb="membe" :t="t" :q="q" :img001="img001" :img002="img002"></seeme>
          </div>
          <div v-else-if="b==9">
            <jinbi :q="jinbi" :m="zhanghao"></jinbi>
          </div>
          <div v-else-if="b==10">
            <jifen :q="jifen" :m="zhanghao"></jifen>

          </div>
        </div>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
  import 学历 from '../assets/personal/学历.png'
  import 学历颜色 from '../assets/personal/学历颜色.png'
  import 手机充值 from '../assets/personal/手机充值.png'
  import 手机充值颜色 from '../assets/personal/手机充值颜色.png'
  import 实名认证 from '../assets/personal/实名认证.png'
  import 实名认证颜色 from '../assets/personal/实名认证颜色.png'
  import 芝麻信用 from '../assets/personal/芝麻信用.png'
  import 芝麻信用颜色 from '../assets/personal/芝麻信用颜色.png'
  import store from '../store';
  import $ from 'jquery'
  window.$ = $;
  window.jQuery = $;
  import 'bootstrap/js/modal'
  import axios from 'axios';

  export default {
    name: 'Personal',
    data() {
      return {
        message:'',
        yi:'',
        name:'',
        phone:'',
        huiyuan:'',
        xiaoxi:'',
        jinbi:0,
        jifen:0,
        fangwen:'12',
        picture:'',
        zhanghao:'',
        b:1,
        name0:'sasaaa',
        t:'4',
        q:'5',
        img001:'',
        img002:''
      }
    },
    mounted: function () {
      store.commit('index_change',3)
      this.check_login()
      this.touxiang();
      this.nameget();
      this.guanzhu();
      this.buy();
      this.dengjirenzheng();

    },
    methods:{
      check_login: function () {
        let _this = this;
        let token = localStorage.getItem('token');
        let id= localStorage.getItem('id')
        if (token) {
          this.axios.get('http://47.106.14.132:8000/user/check_login/', {
            headers: {
              'token': token
            },
            params: {
              id:id
            }
          })
            .then(function (response) {
              let islogin = response.data.islogin
              console.log(response.data)
              if (islogin){
              } else {
                _this.$router.push({path:'/login'})
              }
            })
            .catch(function (error) {
              console.log(error)
              _this.$router.push({path:'/login'})
            })
        }else {
          _this.$router.push({path:'/login'})
        }
      },
      dengjirenzheng:function(){
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/iconchoose/',params)
          .then(function (response) {
            response.data["phone"]==1?vm.phone=手机充值颜色:vm.phone=手机充值;
            response.data["name"]==1?vm.name=实名认证颜色:vm.name=实名认证;
            response.data["friend"]==1?vm.yi=芝麻信用颜色:vm.yi=芝麻信用;
            response.data["message"]==1?vm.message=学历颜色:vm.message=学历;
          });
      },
      buy:function(){
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/money/buymessage/',params)
          .then(function (response) {
            vm.jifen=response.data['integral'];
            vm.jinbi=response.data['balance'];
            vm.zhanghao=response.data['tel'];
            if (vm.jifen<1000){
              vm.huiyuan='普通会员'
            } else if(vm.jifen>1000 && vm.jifen<2000){
              vm.huiyuan='贵族会员'
            }else {
              vm.huiyuan='皇室会员'
            }
          });
        axios.post('http://47.106.14.132:8000/message/getcountmessage/',params)
          .then(function (response) {
            vm.xiaoxi=response.data['message'];
          });
      },
      guanzhu:function(){
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/getfollow/',params)
          .then(function (response) {
            vm.t=response.data['beiguanzhu'].length;
            vm.q=response.data['guanzhu'].length;
            vm.img001=response.data["beiguanzhu"];
            vm.img002=response.data["guanzhu"]
          });
      },
      nameget:function(){
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/nameget/',params)
          .then(function (response) {
            let s0=response.data.name;
            vm.name0=s0
          });
      },
      membe:function (a) {
        this.b=a
      },
      touxiang: function () {
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/xianshitouxiang/',params)
          .then(function (response) {
            let s01=response.data.zhaopian;
            vm.picture=s01

          });
      },
      pic05:function (i) {
        this.picture=i
      },
      namechange05:function (i) {
        this.name0=i
      }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


  .q{
    /*background: #00de00;*/
    color: #666666;
    font-size: 13px;
    padding-top:5px;
    display: flex;
  }
  .q li{
    list-style: none;

  }
  .a{
    margin-top: 10px;
    border: dashed #F23A6E 1px;
  }
  .touxiang{
    width: 120px;
    height: 100%;
    margin-left:47px;
    box-sizing: border-box;
    padding-bottom:5px;
    padding-top: 5px;

  }

  .m {
    padding-left: 15px;
    border-left: solid red 1px;
    max-height:300px;
  }
  .h {
    text-decoration: none;
    color: black;
  }
  .per-img img{
    padding-left: 5px;
  }
  .name{
    font-family:黑体;
    color: #0e0e0e;
    font-size: 30px;
    padding-bottom: 10px;
  }
  .massage{
    padding-left: 20px;
    color:#FF6600;
    /*background: #00de00;*/
  }
  .massage01{
    display: flex;
    list-style: none;
    font-size: 35px;
    text-align: center;
    padding-top: 10px;
    padding-bottom: 10px;

  }
  .massage03{
    padding-left: 20px;
  }
  .massage02{
    font-size: 15px;
    color:#0e0e0e;
  }
  .massage02 a{
    color: #0e0e0e;
    text-decoration: none;
  }
  .massage02 a:hover{
    color:#FF6600;
  }
  .nav-pills > .active > a,
  .nav-pills > .active > a:hover,
  .nav-pills > .active > a:focus {
    color: #ffffff;
    background-color:#F23A6E;
  }
  #myModal .modal-dialog {
    width: 400px;
    height: 100%;
    top: 35%;
    left: 0;
    text-align: center;
  }
  #myModal .modal-content>div{
    margin: 20px 20px 10px 20px;
  }
</style>
