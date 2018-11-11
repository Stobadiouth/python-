<template>
  <div class="container">
    <div class="row">
      <div class="col-md-2">
        <div class="list-group">
          <a href="#" class="list-group-item list-group-item-success" @click="b=1">全部</a>
          <a href="#" class="list-group-item list-group-item-info" @click="b=2">情感文学</a>
          <a href="#" class="list-group-item list-group-item-warning" @click="b=3">恋爱感悟</a>
          <a href="#" class="list-group-item list-group-item-danger" @click="b=4">婚姻家庭</a>
          <a href="#" class="list-group-item list-group-item-success" @click="b=5">单身男女</a>
          <a href="#" class="list-group-item list-group-item-info" @click="b=6">婆媳关系</a>
          <a href="#" class="list-group-item list-group-item-warning" @click="b=7">情感专栏</a>
          <a href="#" class="list-group-item list-group-item-danger" @click="b=8">话题调查</a>
          <a href="#" class="list-group-item list-group-item-success" @click="b=9">转载空间</a>
          <a href="#" class="list-group-item list-group-item-info" @click="b=10">婚姻之道</a>
          <a href="#" class="list-group-item list-group-item-warning" @click="b=11">妯娌姑嫂</a>
          <a href="#" class="list-group-item list-group-item-danger" @click="b=12">亲情友情</a>
          <a href="#" class="list-group-item list-group-item-success" @click="b=13">情感诉求</a>
          <a href="#" class="list-group-item list-group-item-info" @click="b=14">小三故事</a>
          <a href="#" class="list-group-item list-group-item-warning" @click="b=15">恋爱日记</a>
          <a href="#" class="list-group-item list-group-item-danger" @click="b=16">准妈好孕</a>
          <a href="#" class="list-group-item list-group-item-success" @click="b=17">产后交流</a>
          <a href="#" class="list-group-item list-group-item-info" @click="b=18">童梦宝宝</a>
          <a href="#" class="list-group-item list-group-item-warning" @click="b=19">家庭生活</a>
          <a href="#" class="list-group-item list-group-item-danger" @click="b=20">杂七杂八</a>
          <a href="#" class="list-group-item list-group-item-success" @click="b=21">健康养生</a>
          <a href="#" class="list-group-item list-group-item-info" @click="b=22">家有宝贝</a>
          <a href="#" class="list-group-item list-group-item-warning" @click="b=23">教育宝典</a>
        </div>
      </div>
      <div class="col-md-6">
        <ul class="list-group">
          <li class="list-group-item" v-for="t in list" :id="t.id">
            <router-link :to="{name:'Ltxq',params:{invid:t.id}}"><a href="" v-text="t.mainbody" style="font-size: 1.5em"></a></router-link>
            <div>
              <span v-text="'发布时间：'+t.time" style="font-size: 0.8em"></span>
              <span v-text="'发布人'+t.user__name" style="font-size: 0.8em;margin-left: 10px"></span>
            </div>
          </li>
        </ul>
      </div>
      <div>
        <div class="col-md-3">
          <div class="jumbotron">
            <h2>客服咨询</h2>
            <div style="height: 30px"></div>
            <div></div>
            <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&amp;uin=623662999&amp;site=qq&amp;menu=yes"><img
              border="0" src="http://wpa.qq.com/pa?p=2:623662999:7" alt="点这里给我发消息"
              style="width: 106px;height: 36px"></a>
          </div>
          <div class="jumbotron">
            <h2>中国国内最大最好的婚恋相亲网站</h2>
            <p>http://www.meetlo.cn</p>
            <p><a class="btn btn-primary btn-lg" href="#" role="button">点击邂逅</a></p>
          </div>
          <div class="jumbotron">
            <h2>更多关于您的本地相亲活动</h2>
            <p>http://www.meetlo.hd.cn</p>
            <p><a class="btn btn-primary btn-lg" href="#" role="button">点击参加</a></p>
          </div>
        </div>
      </div>
    </div>
    <div id="respond" class="row" style="text-align: center">
      <form id="comment-form" name="comment-form">
        <div class="comment">
          <input name="" class="form-control" size="22" placeholder="提出问题（必填）" maxlength="50" required="required"
                 autocomplete="off" tabindex="1" type="text" style="width: 739px;margin: auto" v-model.trim="title">
          <div class="comment-ctrl">
            <div class="comment-prompt" style="display: none;">
              <i class="fa fa-spin fa-circle-o-notch"></i> <span class="comment-prompt-text">评论正在提交中...请稍后</span></div>
            <div class="comment-success" style="display: none;">
              <i class="fa fa-check"></i> <span class="comment-prompt-text" v-show="success">评论提交成功...</span></div>
            <button tabindex="4" class="btn btn-success" style="margin-top: 20px" @click.prevent.stop="add" :disabled="!islogin">发布问题
            </button>
          </div>
        </div>
      </form>
    </div>
    <nav aria-label="Page navigation" class="fy" style="text-align: center;margin-top: 20px">
      <ul class="pagination">
        <li>
          <a href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li><a href="#">1</a></li>
        <li><a href="#">2</a></li>
        <li><a href="#">3</a></li>
        <li><a href="#">4</a></li>
        <li><a href="#">5</a></li>
        <li>
          <a href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>

</template>

<script>
  import store from '../store';
  export default {
    name: "Luntan",
    data() {
      return {
        title: '',
        id:'',
        islogin: false,
        success:false,
        list: [],
      }
    },
    mounted: function () {
      store.commit('index_change', 4);
      this.check_login();
      let _this = this
      this.axios.get('http://47.106.14.132:8000/forum/getinviation/')
        .then(function (response) {
          _this.list = response.data;
          console.log(response.data);
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    methods: {
      add: function () {
        let _this= this;
        this.axios.get('http://47.106.14.132:8000/forum/addinviation/',{
          params:{
            mainbody:_this.title,
            id:_this.id
          }
        })
          .then(function (response) {
          console.log(response.data);
          if (response.data.code=='409'){
            _this.success=false
          } else {
            _this.list=response.data
            _this.success=true
          }
        })
          .catch(function (error) {
            console.log(error)
          })

      },
      //验证登录
      check_login: function () {
        let _this = this
        let token = localStorage.getItem('token')
        this.id = localStorage.getItem('id')
        if (token) {
          this.axios.get('http://47.106.14.132:8000/user/check_login/', {
            headers: {
              'token': token
            },
            params: {
              id: _this.id
            }
          })
            .then(function (response) {
              _this.islogin = response.data.islogin
              console.log(response.data)
            })
            .catch(function (error) {
              console.log(error)
            })
        }
      },
    },

  }
</script>

<style scoped>
  .container {
    margin: auto;
    padding-top: 20px;
  }

  .tu {
    width: 80px;
    height: 30px;
  }

  .col-md-2 {
    height: 1000px;
    text-align: center;
  }

  .bk {
    color: white;
  }

  .col-md-3 {
    text-align: center;
  }

  .fy {
    text-align: center;
  }

  .jumbotron {
    margin-left: 100px;
    width: 100%;
  }


</style>
