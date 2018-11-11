<template>
  <div>
    <div class="container-fluid header">
      <div class="row">
        <div class="col-md-9"></div>
        <div class="col-md-3 log-reg" v-if="userid">
          <span>ID:{{userid}}</span>&nbsp;/
          <a href="" @click.stop="exit">退出</a>
        </div>
        <div class="col-md-3 log-reg" v-else>
          <router-link to="/login">登录</router-link>/
          <router-link to="/register">注册</router-link>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row nav-head">
        <div class="col-md-4">
          <router-link to="/"><img src="../assets/index/love.png" alt="" class="logo"></router-link>
          <img src="../assets/index/11(1).jpg" alt="" class="logo-text">
        </div>
        <div class="col-md-2"></div>
        <div class="col-md-1" :class="{border:index===1}"><router-link to="/"><a @click="navclick(1)">首页</a></router-link></div>
        <div class="col-md-1" :class="{border:index===2}"><router-link to="/search"><a @click="navclick(2)">搜索</a></router-link></div>
        <div class="col-md-1" :class="{border:index===3}"><router-link to="/personal"><a @click="navclick(3)">个人中心</a></router-link></div>
        <div class="col-md-1" :class="{border:index===4}"><router-link to="/luntan"><a @click="navclick(4)">论坛</a></router-link></div>
        <div class="col-md-1" :class="{border:index===5}"><router-link to="/active"><a @click="navclick(5)">活动</a></router-link></div>
        <div class="col-md-1" :class="{border:index===6}"><router-link to="/email"><a @click="navclick(6)">邮箱</a></router-link></div>
      </div>
    </div>
    <div class="blue-line"></div>
  </div>
</template>

<script>
  import store from '../store'
export default {
  name: 'NavHeader',
  data () {
    return {
      userid:null
    }
  },
  methods:{
    exit:function () {
      sessionStorage.clear();
      localStorage.clear()
    },
    navclick:function (i) {
      store.commit('index_change',i)
    }
  },
  created:function () {
    this.userid=localStorage.getItem('id')
    console.log(this.userid)
  },
  computed:{
    index(){
      return store.state.index
    },
    user_id(){
      return store.state.user_id
    }
  },
  watch:{
    user_id:function () {
      this.userid=this.user_id
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body,ul,li,table,div,a,input{
    padding: 0 ;
    margin: 0 ;
    box-sizing: border-box;
  }
  a{
    text-decoration: none !important;
  }
  a:hover{
    text-decoration: solid underline white !important;
  }
  li{
    list-style: none;
    background: rgba(255,0,0,0);
    float: left;
  }

  /*         header           */
  .header{
    height: 32px;
    background: #F23A6E;
  }
  .log-reg{
    height: 32px;
    text-align: center;
    line-height: 32px;
    color: white;
  }
  .log-reg a{
    color: white!important;
  }

  /*--------neck--------*/
  .nav-head div{
    height:50px;
    text-align: center;
    line-height: 50px;
  }
  .logo{
    width: 30%;
    height: 80%;
    margin-top: 5px;
  }
  .logo-text{
    width: 50%;
    height: 60%;
    margin-top: 10px;
  }
  .nav-head div{

  }
  .nav-head a{
    color: black;
    font-size: medium;
  }
  .nav-head a:hover{
    color: #F23A6E;
  }

  .blue-line{
    background: rgba(0, 0, 228, 0.28);
    height: 1px;
  }
  .border{
    border-bottom: 2px solid #F23A6E;;
  }
  .container{
    margin: auto;
  }
</style>
