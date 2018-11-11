<template>
  <div class="container">
    <div class="row message">
      <div class="col-md-4 left pre-scrollable">
        <div class="blue">
          <span>所有消息</span>
          <span class="glyphicon glyphicon-comment" aria-hidden="true"></span>
        </div>
        <div @click="count=1" :class="{white:count===1}">
          <span>验证消息</span>
          <span class="glyphicon glyphicon-bell" aria-hidden="true"></span>
        </div>
        <div v-for="r in rfriends" @click.stop="getemail(r.sendid)" :class="{white:count===r.sendid}">
          <span v-text="r.sendid__name"></span>
          <span class="glyphicon glyphicon-remove" @click.stop="remove(r.sendid)"></span>
        </div>
        <div v-for="r in sfriends" @click.stop="getemail(r.receiveid)" :class="{white:count===r.receiveid}">
          <span v-text="r.receiveid__name"></span>
          <span class="glyphicon glyphicon-remove" @click.stop="remove(r.receiveid)"></span>
        </div>
      </div>
      <!--模态框-->
      <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content loginmodal">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                &times;
              </button>
              <h4 class="modal-title" id="myModalLabel">
                确定删除此好友吗
              </h4>
            </div>
            <div>
              <button type="button" class="btn btn-default" data-dismiss="modal">取消
              </button>
              <button type="button" class="btn btn-primary" data-dismiss="modal" @click="removesure">
                确定
              </button>
            </div>
          </div><!-- /.modal-content -->
        </div><!-- /.modal -->
      </div>
      <div class="col-md-8 right">
        <div class="friend" v-if="count===1">
          <div v-for="r in frequest">
            <router-link :to="{name:'member',params:{userid:r.sendid}}"><span v-text="r.sendid__name"></span></router-link>&nbsp;<span>请求添加你为好友</span>
            <div><button @click.stop="agree(r.sendid)">同意</button><button @click.stop="refuse(r.sendid)">拒绝</button></div>
          </div>
        </div>
        <div v-else>
          <div class="email pre-scrollable">
            <div v-for="e in emails">
              <router-link :to="{name:'member',params:{userid:e.senduser}}"><span v-text="e.senduser__name"></span></router-link><span v-text="e.sendtime"></span>
              <p v-text="e.content"></p>
            </div>
          </div>
          <div class="reply">
            <textarea class="form-control" rows="4" v-model.trim="reply"></textarea>
            <div><button class="btn" @click.stop="sendmessage">回复</button></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import store from '../store';
  import $ from 'jquery'
  window.$ = $;
  window.jQuery = $;
  import 'bootstrap/js/modal'

export default {
  name: 'Email',
  data () {
    return {
      id:'',
      islogin:false,
      count:1,
      frequest:[],
      rfriends:[],
      sfriends:[],
      emails:[],
      reply:'',
      receiveid:''
    }
  },
  created:function () {
    store.commit('index_change',6);
    this.check_login();
  },
  methods:{
    check_login: function () {
      let _this = this;
      let token = localStorage.getItem('token');
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
            _this.getrequest()
            _this.getfriends()
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    getrequest:function(){
      let _this=this
      if (this.islogin){
        this.axios.get('http://47.106.14.132:8000/message/frequest/',{
          params:{
            id:_this.id
          }
        })
          .then(function (response) {
            _this.frequest=response.data
            console.log(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      }
    },
    agree:function (i) {
      let _this=this
      this.axios.get('http://47.106.14.132:8000/message/agree/',{
        params:{
          sendid:i,
          receiveid:_this.id
        }
      })
        .then(function (response) {
          _this.frequest=response.data.request
          _this.rfriends=response.data.rfriends;
          _this.sfriends=response.data.sfriends
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    refuse:function (i) {
      let _this=this
      this.axios.get('http://47.106.14.132:8000/message/refuse/',{
        params:{
          sendid:i,
          receiveid:_this.id
        }
      })
        .then(function (response) {
          _this.frequest=response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getfriends:function () {
      let _this=this;
      this.axios.get('http://47.106.14.132:8000/message/friends/',{
        params:{
          id:_this.id
        }
      })
        .then(function (response) {
          _this.rfriends=response.data.rfriends;
          _this.sfriends=response.data.sfriends
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    getemail:function (i) {
      this.count=i
      this.receiveid=i;
      let _this=this
      this.axios.get('http://47.106.14.132:8000/message/getemails/',{
        params:{
          id1:_this.id,
          id2:i
        }
      })
        .then(function (response) {
          _this.emails=response.data
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    sendmessage:function () {
      let _this=this
      this.axios.get('http://47.106.14.132:8000/message/addmessage/',{
        params:{
          senduser:_this.id,
          receiveuser:_this.receiveid,
          message:_this.reply
        }
      })
        .then(function (response) {
          let date=new Date();
          date=date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate()+' '+date.getHours()+':'+
            date.getMinutes()+':'+date.getSeconds();
          let message={"senduser":_this.id,"senduser__name":"我","sendtime":date,"content":_this.reply}
          _this.emails.push(message)
          _this.reply='';
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    remove:function (i) {
      $('#myModal').modal('show');
      this.receiveid=i
    },
    removesure:function () {
      let _this=this
      this.axios.get('http://47.106.14.132:8000/message/remove/',{
        params: {
          id1: _this.id,
          id2: _this.receiveid
        }
      })
        .then(function (response) {
          console.log(response.data);
          if (response.data.code=="202"){
            _this.count=1
            _this.getfriends()
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  div{
    box-sizing: border-box;
  }
  .white{
    background: white!important;
  }
  .message{
    width: 80%;
    height: 600px;
    margin: auto;
    border: 1px grey dashed;
    margin-top: 40px;
  }
  .left{
    min-height: 100%;
    padding: 0;
    overflow-y:auto;
    background: rgba(214, 214, 214, 0.48);
  }
  .left>div{
    text-align: center;
    height: 50px;
    line-height: 50px;
    border-bottom: 1px grey solid;
    cursor: pointer;
  }
  .left>div span{
    font-size: 1.2em;
    margin-right: 5px;
  }
  .blue{
    background: lightpink!important;
  }
  .right{
    min-height: 100%;
    overflow-y: auto;
    background: rgba(255, 255, 212, 0.24);
  }
  .friend>div{
    margin-top: 20px;
    background: rgba(173, 216, 230, 0.39);
    padding: 5px;
    border-radius: 5px;
    box-shadow: 1px 1px 1px 1px;
  }
  .friend button{
    margin-left: 10px;
    width: 80px;
    height: 25px;
    background: white;
  }
  .friend>div div{
    text-align: right;
  }
  .email{
    min-height: 450px;
    overflow-y: auto;
  }
  .email>div{
    margin-top: 20px;
  }
  .email>div a span{
    font-size: large;
    color: black;
  }
  .email>div span{
    font-size: small;
    margin-left: 10px;
    color: grey;
  }
  .email>div p{
    background: white;
    padding: 5px;
    word-wrap:break-word;
    word-break:break-all;
    overflow: hidden;
    margin-top: 5px;
  }
  .reply{
    height: 150px;
  }
  .reply div{
    margin-top: 10px;
    text-align: right;
  }
  .reply button{
    background: #D86EA3;
    color: white;
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
