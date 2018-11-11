<template>
  <div class="container">
      <!--搜索框-->
      <div class="row middle">
        <div class="col-md-9">
          <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
              <li class="left-search">
                <input type="text" placeholder="请输入要搜索的条件" v-model.trim="con" @keyup.enter="search()">
              </li>
              <button class="left-btn" @click="search()">搜索</button>
            </div>
            <div class="col-md-1"></div>
          </div>
          <ul class="row left-hot">
            <li>热门搜索词：</li>
            <li v-for="word in hotwords" v-text="word.word" @click="toSearch(word.word)"></li>
          </ul>
        </div>
        <div class="col-md-3" v-if="login">
          <div class="right-login" style="background: rgba(210,210,210,0.68)">
            <router-link to="/personal" v-if="img_src"><img :src="img_src" alt="" class="img-circle head"></router-link>
            <router-link to="/personal" v-else><img src="../assets/index/headdefault.jpg" alt="" class="img-circle head"></router-link>
            <p>你好，{{name}}</p>
          </div>
        </div>
        <div class="col-md-3" v-else>
          <div class="right-login">
            <img src="../assets/index_icon/cc-head.svg" alt="">
            <p>Hi&nbsp;!&nbsp;你好</p>
            <router-link to="/login"><button class="btn active">登录</button></router-link>
            <router-link to="/register"><button class="btn active">注册</button></router-link>
          </div>
        </div>
      </div>
      <div class="blue-line"></div>
      <div class="main">
        <ul class="row main-title">
          <li><img src="../assets/index_icon/heart.svg" alt="">为你推荐</li>
          <li @click.stop="tagClick1">同城人</li>
          <li @click.stop="tagClick2">爱电影</li>
          <li @click.stop="tagClick3">同美食</li>
          <li @click.stop="tagClick4">爱宠物</li>
          <li @click.stop="tagClick5">90后</li>
        </ul>
        <div class="row list">
          <div class="col-md-2" v-for="user in users" :key="user.id" :id="user.id">
            <div><router-link :to="{name:'member',params:{userid:user.id}}"><img :src="user.img_src" alt=""></router-link></div>
            <div><p v-text="user.name"></p><p v-text="user.birth+'岁'"></p><p v-text="user.height+'CM'"></p></div>
          </div>
        </div>
        <ul class="row main-title">
          <li><img src="../assets/index_icon/爱心.svg" alt="">晒幸福</li>
        </ul>
        <div class="row show">
            <div class="col-md-5"><img src="../assets/index/show_right1.jpg" alt=""></div>
            <div class="col-md-5"><img src="../assets/index/show_right2.jpg" alt=""></div>
            <div class="col-md-5"><img src="../assets/index/show_right3.jpg" alt=""></div>
            <div class="col-md-5"><img src="../assets/index/show_right4.jpg" alt=""></div>
        </div>
      </div>
    </div>
</template>

<script>

  import store from '../store';
export default {
  name: 'Home',
  data () {
    return {
      login:false,
      name:null,
      img_src:null,
      sex:'',
      users:[],
      hotwords:[],
      city:'',
      con:''
    }
  },
  mounted:function () {
    store.commit('index_change',1);
    this.islogin();
    this.getwords()
    this.getUsers()
  },
  methods:{
    islogin:function () {
      let _this=this;
      let token=localStorage.getItem('token');
      let userid=localStorage.getItem('id');
      if (token){
        this.login=true;
        this.axios.get('http://47.106.14.132:8000/user/getuser/',{
          params:{
            id:userid
          }
        })
          .then(function (response) {
            _this.name=response.data.name;
            _this.img_src=response.data.img_src;
            _this.sex=response.data.sex_id;
            localStorage.setItem('sex_id',_this.sex);
            _this.city=response.data.city;
            console.log(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    getUsers:function () {
      let _this=this;
      console.log(this.sex)
      this.axios.get('http://47.106.14.132:8000/user/index_users/',{
        params:{
          sex_id:_this.sex
        }
      })
        .then(function (response) {
          _this.users=response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    tagClick1:function () {
      let _this=this;
      this.axios.get('http://47.106.14.132:8000/user/getcity/',{
        params:{
          sex_id:_this.sex,
          city:_this.city
        }
      })
        .then(function (response) {
          _this.users=response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    tagClick2:function () {
      let _this=this;
      this.axios.get('http://47.106.14.132:8000/user/getfilm/',{
        params:{
          sex_id:_this.sex,
        }
      })
        .then(function (response) {
          _this.users=response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    tagClick3:function () {
      let _this=this;
      this.axios.get('http://47.106.14.132:8000/user/getfood/',{
        params:{
          sex_id:_this.sex,
        }
      })
        .then(function (response) {
          _this.users=response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    tagClick4:function () {
      let _this=this;
      this.axios.get('http://47.106.14.132:8000/user/getpet/',{
        params:{
          sex_id:_this.sex,
        }
      })
        .then(function (response) {
          _this.users=response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    tagClick5:function () {
      let _this=this;
      this.axios.get('http://47.106.14.132:8000/user/get90/',{
        params:{
          sex_id:_this.sex,
        }
      })
        .then(function (response) {
          _this.users=response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    search:function () {
      let _this=this;
      if (this.con){
        this.axios.get('http://47.106.14.132:8000/search/addword/',{
          params:{
            con:_this.con
          }
        })
          .then(function (response) {
            console.log(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
      _this.$router.push({path:'/search',query:{"con":_this.con}})
    },
    toSearch:function(i){
      this.con=i;
      this.search()
    },
    getwords:function () {
      let _this=this
      this.axios.get('http://47.106.14.132:8000/search/getwords/')
        .then(function (response) {
          _this.hotwords=response.data;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  },
  watch:{
    sex:function () {
      this.getUsers()
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
  li{
    list-style: none;
    background: rgba(255,0,0,0);
    float: left;
  }
  .container{
    margin: auto;
  }
  .blue-line{
    background: rgba(0, 0, 228, 0.28);
    height: 1px;
  }
  /*--------middle-------*/
  .middle{
    overflow: hidden;
    width: 100%;
    height: 200px;
    background: url("../assets/index/loveheart.png");
    background-size: contain;
  }
  .middle .left-search{
    width: 80%;
    height: 50px;
    border: solid 5px #F23A6E;
    background: white;
    margin-top: 100px;
  }
  .left-search input{
    width: 100%;
    height: 100%;
    outline: none;
    border: none;
  }
  .left-btn{
    width: 20%;
    height: 50px;
    background: #F23A6E;
    color: white;
    font-size: 1.2em;
    letter-spacing: 5px;
    border: none;
    margin-top: 100px;
  }
  .middle .left-hot{
    margin-top: 20px;
    margin-left: 70px;
  }
  .left-hot li{
    margin-right: 20px;
    color: #F23A6E;
    cursor: pointer;
  }
  .left-hot li:nth-of-type(1){
    color: black;
  }

  .right-login{
    height: 140px;
    width: 190px;
    margin: auto;
    margin-top: 60px;
    background: rgba(255, 0, 0, 0.15);
    text-align: center;
    padding-top: 10px;
  }
  .head{
    width: 80px;
    height: 80px;
    margin-bottom: 10px;
  }

  .right-login button{
    border: solid 1px lightpink;
    padding: 0;
    width: 70px;
    height: 30px;
    background: rgba(173, 216, 230, 0.31);
    color: black;
  }

  /*-----------css----------*/
  .main{
    width: 100%;
    padding-top: 30px;
    padding-left: 10px;
    padding-right: 10px;
    background: url("../assets/index/flower.png");
    background-position:570px 600px;
  }

  .main-title li:nth-of-type(1){
    color: black;
    font-weight: normal;
    font-size: 1.5em;
  }
  .main-title li{
    cursor: pointer;
    margin-right: 20px;
    font-size: 1.2em;
    color: rgba(49, 24, 76, 0.7);
    font-weight: bold;
  }

  .list>div{
    padding: 0;
    margin: 20px 20px 40px 20px;
    width: 190px;
    box-shadow: 1px 1px 1px 1px #ff7976;
    background-size: cover;
  }

  .list>div div:nth-of-type(1){
    width: 100%;
    height: 240px;
  }
  .list>div div:nth-of-type(1) img{
    width: 100%;
    height: 100%;
  }
  .list>div div:nth-of-type(1) img:hover{
    opacity: 0.8;
  }
  .list>div div:nth-of-type(2){
    width: 100%;
    color: grey;
    text-align: center;
    background: white;
  }
  .show{
    width: 100%;
    margin-top: 30px;
    box-shadow: 2px 2px 1px 1px rgba(106, 147, 190, 0.57);
  }
  .show>div{
    height: 250px;
    margin-left: 60px;
    margin-top: 20px;
  }
  .show img{
    width: 100%;
    height: 100%;
  }


</style>
