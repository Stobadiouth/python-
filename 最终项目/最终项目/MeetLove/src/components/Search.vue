<template>
  <div class="container">
    <div class="row search">
      <div class="col-md-9">
        <p style="color: white;font-family: 华文琥珀;font-size:20px;margin-top: -5px">选择条件：</p>
        <div style="border: solid white 2px;height: 60px; margin-left:90px;margin-right: 10px;float: left;"></div>
        <form class="form-inline" role="form">
          <select v-model="sex" class="form-control">
            <option value="0">女</option>
            <option value="1">男</option>
          </select>
          <select v-model="age" class="form-control">
            <option value="25">25岁以下</option>
            <option value="35">25-35岁</option>
            <option value="45">35-45岁</option>
            <option value="100">45岁以上</option>
          </select>
          <sele-ss @selectpro="getprov" @selectcity="getcity"></sele-ss>
          <select v-model="edu" class="form-control">
            <option value="1">高中及以下</option>
            <option value="2">中专</option>
            <option value="3">大专</option>
            <option value="4">本科</option>
            <option value="5">硕士</option>
            <option value="6">博士</option>
          </select>
          <select v-model="income" class="form-control">
            <option value="1">1-5万元</option>
            <option value="2">5-10万元</option>
            <option value="3">10-15万元</option>
            <option value="4">15-20万元</option>
            <option value="5">20-35万元</option>
            <option value="6">35-50万元</option>
            <option value="7">50-100万元</option>
            <option value="8">100万元以上</option>
          </select>
          <select v-model="height" class="form-control">
            <option value="150">150cm以下</option>
            <option value="160">150-160cm</option>
            <option value="165">160-165cm</option>
            <option value="170">165-170cm</option>
            <option value="175">170-175cm</option>
            <option value="180">175-180cm</option>
            <option value="190">180-190cm</option>
            <option value="300">190cm以上</option>
          </select>
        </form>
        <div style="border: solid white 0.5px;width: 300px; left:60px;margin-top: 10px;position: absolute;"></div>
      </div>
      <div class="col-md-3">
        <button class="btn" @click.stop="search">搜索</button>
      </div>
    </div>
    <div class="list">
      <ul class="row">
        <li>排序方式：</li>
        <li :class="{liactive:li===1}" @click="order(1,'id')">默认</li>
        <li :class="{liactive:li===2}" @click="order(2,'birth')">年龄<img src="../assets/search/down.svg" ></li>
        <li :class="{liactive:li===3}" @click="order(3,'income_id')">收入<img src="../assets/search/down.svg"></li>
        <li :class="{liactive:li===4}" @click="order(4,'height')">身高<img src="../assets/search/down.svg"></li>
      </ul>
      <div class="row">
        <div class="col-md-2 pin" v-for="user in users" :key="user.id" :id="user.id">
          <router-link :to="{name:'member',params:{userid:user.id}}"><div class="img"><img :src="user.img_src" alt=""></div></router-link>
          <div class="name" v-text="user.name"></div>
          <div class="message">
            <span v-text="user.birth"></span>
            <span v-text="user.city"></span>
          </div>
          <div class="db">
            <p>爱情宣言</p>
            <textarea v-text="user.signature" class="form-control" readonly></textarea>
          </div>
        </div>
      </div>
    </div>
    <nav class="pages">
      <ul class="pagination">
        <li @click="last">上一页</li>
        <li :class="{pageactive:page===i}" v-for="i in pages" @click="paging(i)" v-show="page-4<i && i<page+4">{{i}}</li>
        <li @click="next">下一页</li>
      </ul>
    </nav>
  </div>
</template>

<script>
  import $ from 'jquery'
  import store from '../store';
export default {
  name: 'Search',
  data () {
    return {
      con:'',
      sex_id:'',
      users:[],
      pages:0,
      page:1,
      li:1,
      sex:0,
      age:25,
      prov:'',
      city:'',
      edu:1,
      income:1,
      height:150,
      condition:{}
    }
  },
  created:function () {
    store.commit('index_change',2);
    this.initUsers()
  },
  methods: {
    //初始化页面
    initUsers: function () {
      let _this = this;
      this.con = this.$route.query.con;
      this.sex_id = localStorage.getItem('sex_id');
      this.axios.get('http://47.106.14.132:8000/user/search_users/', {
        params: {
          con: _this.con,
          sex_id: _this.sex_id,
          index:_this.page
        }
      })
        .then(function (response) {
          _this.users = response.data.users;
          _this.pages=response.data.pagescount;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    //点击翻页
    paging:function (i) {
      let _this=this;
      this.page=i;
      this.li=1;
      if (this.condition.index) {
        this.condition.index=this.page;
        $.ajax({
          url:'http://47.106.14.132:8000/user/btn_search/',
          type:"POST",
          data:JSON.stringify(_this.condition),
          dataType:"json",
          contentType:"application/json",
          success:function (response,textStatus,xhr) {
            console.log(response);
            console.log(textStatus);
            _this.users=response['users'];
            _this.pages=response['pagescount']
            // console.log(request.getAllResponseHeaders())
          },
          error:function (XMLHttpRequest,textStatus,errorThrown) {
            console.log('nononon');
            console.log(textStatus)
          }
        })
      }else {
        this.axios.get('http://47.106.14.132:8000/user/search_users/', {
          params: {
            con: _this.con,
            sex_id: _this.sex_id,
            index:_this.page
          }
        })
          .then(function (response) {
            _this.users = response.data.users;
            _this.pages=response.data.pagescount;
            console.log(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    //上一页
    last:function(){
      if (this.page>1){
        this.paging(this.page-1)
      }
    },
    //下一页
    next:function(){
      if (this.page<this.pages){
        this.paging(this.page+1)
      }
    },
    compare:function (prop) {
      return function (obj1, obj2) {
        let val1 = obj1[prop];
        let val2 = obj2[prop];if (val1 < val2) {
          return -1;
        } else if (val1 > val2) {
          return 1;
        } else {
          return 0;
        }
      }
    },
    //排序
    order:function (i,prop) {
      this.li=i;
      this.users.sort(this.compare(prop)).reverse()
    },
    //获取省
    getprov:function (i) {
      this.prov=i
    },
    //获取市
    getcity:function (i) {
      this.city=i
    },
    //搜索
    search:function () {
      let _this=this;
      this.page=1;
      this.li=1
      this.condition={};
      this.condition.sex=this.sex;
      let date=new Date();
      this.condition.age=String(date.getFullYear()-this.age)+'-1-1';
      this.condition.city=this.prov+this.city;
      this.condition.edu=this.edu;
      this.condition.income=this.income;
      this.condition.height=this.height;
      this.condition.index=this.page;
      $.ajax({
        url:'http://47.106.14.132:8000/user/btn_search/',
        type:"POST",
        data:JSON.stringify(_this.condition),
        dataType:"json",
        contentType:"application/json",
        success:function (response,textStatus,xhr) {
          console.log(response);
          console.log(textStatus);
          _this.users=response['users'];
          _this.pages=response['pagescount']
          // console.log(request.getAllResponseHeaders())
        },
        error:function (XMLHttpRequest,textStatus,errorThrown) {
          console.log('nononon');
          console.log(textStatus)
        }
      })
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
  .search{
    width: 100%;
    height: 180px;
    background: url("../assets/search/searchbg.jpg");
    background-size: contain;
    padding-top: 60px;
    padding-left: 40px;
    overflow: hidden;
  }
  select {
    appearance: none;
    -moz-appearance: none;
    -webkit-appearance: none;
    background: rgba(32, 178, 170, 0.56);
    font-size: 15px;
    color: #000;
    border:solid rgba(249, 249, 249, 0.67) 1px;
  }



  .search .btn{
    width: 100px;
    height: 40px;
    margin-top: 30px;
    background: rgba(0, 0, 143, 0.55);
    color: lightblue;
    font-size: 1.2em;
  }

  .list{
    width: 100%;
    margin-top: 40px;
    padding-left: 10px;
    padding-right: 10px;
  }
  .list ul{
    margin-top: 50px;
  }
  .list li{
    margin-right: 20px;
    border: rgba(128, 128, 128, 0.53) 1px solid;
    background: rgba(173, 173, 173, 0);
    cursor: pointer;
  }
  .list li:nth-of-type(1){
    border: none;
    background: none;
  }
  .list .liactive{
    background: rgba(255, 182, 193, 0.76);
  }

  .list .pin{
    height: 390px;
    margin: 20px 10px 40px 20px;
    border: dashed #BBD9D1 2px;
    padding: 5px;
    text-align: center;
  }
  .list .pin:hover{
    box-shadow: 2px 2px 2px 2px #BBD9D1;
    border: none;
  }

  .pin .img{
    height: 220px;
    width: 100%;
    margin-bottom: 10px;
  }
  .pin img{
    height: 100%;
    width: 100%;
  }

  .name{
    color: grey;
  }
  .message{
    font-size: 0.8em;
    margin-bottom: 10px;
  }
  .db p{
    margin: 0;
    font-size: 0.8em;
    font-weight: bold;
  }
  .db textarea{
    margin-top: 5px;
    height: 75px;
    width: 175px;
    color: grey;
    overflow : hidden;
    text-overflow: ellipsis;
    background: rgba(173, 216, 230, 0.53);
    border: none;
  }

  .pages{

    text-align: center;
    padding-top: 30px;
  }
  .pages li{
    color: grey;
    border: solid 1px grey;
    width: 60px;
    height: 30px;
    line-height: 30px;
    box-shadow: 1px 1px 1px 1px grey;
    border-radius: 5px;
    cursor: pointer;
  }
  .pageactive{
    background: lightblue;
  }

</style>
