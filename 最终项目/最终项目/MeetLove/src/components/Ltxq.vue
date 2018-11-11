<template>
  <div class="row container">
    <div class="col-md-2">
      <div class="list-group">
        <a href="#" class="list-group-item list-group-item-success">全部</a>
        <a href="#" class="list-group-item list-group-item-info">情感文学</a>
        <a href="#" class="list-group-item list-group-item-warning">恋爱感悟</a>
        <a href="#" class="list-group-item list-group-item-danger">婚姻家庭</a>
        <a href="#" class="list-group-item list-group-item-success">单身男女</a>
        <a href="#" class="list-group-item list-group-item-info">婆媳关系</a>
        <a href="#" class="list-group-item list-group-item-warning">情感专栏</a>
        <a href="#" class="list-group-item list-group-item-danger">话题调查</a>
        <a href="#" class="list-group-item list-group-item-success">转载空间</a>
        <a href="#" class="list-group-item list-group-item-info">婚姻之道</a>
        <a href="#" class="list-group-item list-group-item-warning">妯娌姑嫂</a>
        <a href="#" class="list-group-item list-group-item-danger">亲情友情</a>
        <a href="#" class="list-group-item list-group-item-success">情感诉求</a>
        <a href="#" class="list-group-item list-group-item-info">小三故事</a>
        <a href="#" class="list-group-item list-group-item-warning">恋爱日记</a>
        <a href="#" class="list-group-item list-group-item-danger">准妈好孕</a>
        <a href="#" class="list-group-item list-group-item-success">产后交流</a>
        <a href="#" class="list-group-item list-group-item-info">童梦宝宝</a>
        <a href="#" class="list-group-item list-group-item-warning">家庭生活</a>
        <a href="#" class="list-group-item list-group-item-danger">杂七杂八</a>
        <a href="#" class="list-group-item list-group-item-success">健康养生</a>
        <a href="#" class="list-group-item list-group-item-info">家有宝贝</a>
        <a href="#" class="list-group-item list-group-item-warning">教育宝典</a>
      </div>
    </div>
    <div class="col-md-10">
      <div class="zbk">
        <a href="">遇见爱官方网站</a>»<a href="">遇见爱官方论坛</a>»<a href="">全部»</a>
      </div>
      <div class="btn-group  btn-group-sm" role="group" aria-label="...">
        <router-link to='/Luntan'>
          <button type="button" class="btn btn-default" style="height: 30px">返回</button>
        </router-link>
      </div>
      <div class="btl" style="width: 100%;height: 30px;background: linear-gradient(to bottom,#C1D9F1,#E6EFF4);padding-top: 5px">
        [<a href="" style="color: #2C459C;">全部</a>]
      </div>
      <div class="btl" style="width: 100%;height: 30px;padding-top: 5px;border-bottom: #D9E6BB solid 1px;text-align: center">
        <p>阅读量：68409
          回复量：148
          收藏量：80</p>
      </div>
      <div class="col-md-10" style="height: 800px">
        <div style="text-align: center">
          <h2 v-text="inviation[0].mainbody"></h2>
          <div>
            <span v-text="'发布者'+inviation[0].user__name"></span><span v-text="'时间'+inviation[0].time" style="margin-left: 20px"></span>
          </div>
        </div>
        <div v-for="q in list" style="margin-top: 40px;border-top: 1px grey solid">
          <div style="font-size: 1.2em"><span v-text="q.user__name"></span><span v-text="q.time" style="margin-left: 20px"></span></div>
          <h3 v-text="q.content"></h3>
        </div>
      </div>
    </div>

    <div id="respond" style="width: 740px;margin: 0 auto">
      <form id="comment-form" name="comment-form">
        <div class="comment">
          <textarea placeholder="您的评论或留言（必填）" name="comment-textarea" id="comment-textarea" cols="100%" rows="3" tabindex="3" type="text" v-model.trim="comment"></textarea>
          <!--<input name=""  class="form-control" size="22" placeholder="请输入评论或回复" maxlength="500"  required="required" autocomplete="off" tabindex="1" type="text" style="width: 740px;height: 300px" v-model="quanwen">-->
          <div class="comment-ctrl" style="text-align: center">
            <div class="comment-prompt" style="display: none;"><i class="fa fa-spin fa-circle-o-notch"></i>
              <span class="comment-prompt-text">评论正在提交中...请稍后</span></div>
            <div class="comment-success" style="display: none;"><i class="fa fa-check"></i>
              <span class="comment-prompt-text">评论提交成功...</span></div>
            <button tabindex="4" class="btn btn-success" style="margin-top: 20px" @click.prevent.stop="add" :disabled="!islogin">发表评论</button>
          </div>
        </div>
      </form>
    </div>
    <nav aria-label="Page navigation" class="fy" style="text-align: center;">
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
  export default {
    name: "Ltxq",
    data() {
      return {
        invid: '',
        comment: '',
        islogin: false,
        list: [],
        id:'',
        inviation:[{"inviation":'加载中',"user__name":'加载中',"time":'加载中'}]
      }
    },
    mounted: function () {
      this.invid = this.$route.params.invid;
      this.check_login();
      let _this=this
      this.axios.get('http://47.106.14.132:8000/forum/getcomment/',{
        params:{
          invid:_this.invid
        }
      })
        .then(function (response) {
          _this.list = response.data.comment;
          _this.inviation=response.data.inviation
          console.log(response.data);
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    methods: {
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
    //  添加评论
      add:function () {
        let _this=this
        this.axios.get('http://47.106.14.132:8000/forum/addcomment/',{
          params:{
            invid:_this.invid,
            userid:_this.id,
            content:_this.comment
          }
        })
          .then(function (response) {
            console.log(response.data);
            if (response.data.code=='409'){
            } else {
              _this.list=response.data
            }
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    }
  }
</script>

<style scoped>
  .container {
    margin: auto;
    padding-top: 20px;
    padding-bottom: 40px;
  }

  .col-md-2 {
    height: 1000px;
    text-align: center;
  }

  .fy {
    text-align: center;
  }

</style>
