<template>
  <div class="container">
    <div class="row">
      <div class="col-md-3">
        <img :src="user_base.img_src" class="left" alt="">
      </div>
      <div class="col-md-9 right">
        <div class="div-name" v-text="user_base.name"></div>
        <div class="div-id" v-text="'loveid:'+userid"></div>
        <div class="under">
          <div class="row div-col">
            <div class="col-md-4" v-text="'年龄：'+user_base.birth"></div>
            <div class="col-md-4">身高：{{user_base.height}}</div>
            <div class="col-md-4">年收入：{{user_base.income__income}}</div>
          </div>
          <div class="div-line"></div>
          <div class="row div-col">
            <div class="col-md-4">婚况：{{user_base.marry}}</div>
            <div class="col-md-4">学历：{{user_base.edu__edu}}</div>
            <div class="col-md-4">工作地：{{user_base.city}}</div>
          </div>
          <div class="div-line"></div>
          <div class="div-col title">爱情宣言</div>
          <p v-text="user_base.signature"></p>
        </div>
        <div style="margin-left: 30px">
          <button class="btn btn-primary mybtn" @click="sendemail">发消息</button>
          <button class="btn btn-success mybtn" @click="addfriend" v-text="btn2"></button>
          <button class="btn btn-info mybtn" @click="like" v-text="btn3"></button>
        </div>
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
              登录
            </h4>
          </div>
          <div class="input">
            <input type="text" class="form-control" placeholder="账号" v-model="tel">
            <input type="password" class="form-control" placeholder="password" v-model="password">
          </div>
          <p v-show="error" id="error">用户名或密码错误</p>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭
            </button>
            <button type="button" class="btn btn-primary" @click="login_in">
              登录
            </button>
          </div>
        </div><!-- /.modal-content -->
      </div><!-- /.modal -->
    </div>
    <div class="modal fade" id="messageModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
            <h4 class="modal-title" id="exampleModalLabel">发送消息</h4>
          </div>
          <div class="modal-body">
            <form>
              <div class="form-group">
                <label for="message-text" class="control-label">消息:</label>
                <textarea class="form-control" id="message-text" v-model.trim="message"></textarea>
              </div>
            </form>
          </div>
          <p v-show="fail" id="messageerror" class="text-error">发送失败</p>
          <p v-show="success" id="messagesuccess" class="text-success">发送成功</p>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="seedmessage">发送</button>
          </div>
        </div>
      </div>
    </div>
    <div class="center">
      <div class="row">
        <div class="col-md-3">
          <div class="div-orange">
            <img src="../assets/member_icon/文件.svg" alt="">
          </div>
          <p class="div-name" style="margin-left: 85px;margin-top: 10px">详细资料</p>
        </div>
        <div class="col-md-9">
          <div class="row center-right">
            <div class="col-md-4">
              <div>籍贯：{{user_mess.addr}}</div>
              <div>体重：{{user_mess.weight}}kg</div>
              <div>星座：{{user_mess.constellation}}</div>
            </div>
            <div class="col-md-4">
              <div>血型：{{user_mess.blood}}</div>
              <div>民族：{{user_mess.nation}}</div>
              <div>职业：{{user_mess.profession}}</div>
            </div>
            <div class="col-md-4">
              <div>住房条件：{{user_mess.house}}</div>
              <div>有无孩子：{{user_mess.children}}</div>
              <div>毕业学校：{{user_mess.school}}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="center">
      <div class="row">
        <div class="col-md-3">
          <div class="div-orange">
            <img src="../assets/member_icon/house.svg" alt="">
          </div>
          <p class="div-name" style="margin-left: 85px;margin-top: 10px">生活状况</p>
        </div>
        <div class="col-md-9">
          <div class="row center-right">
            <div class="col-md-4">
              <div>是否喝酒：{{user_life.drink}}</div>
              <div>是否抽烟：{{user_life.smoke}}</div>
            </div>
            <div class="col-md-4">
              <div>是否购车：{{user_life.car}}</div>
              <div>厨艺：{{user_life.cook}}</div>
            </div>
            <div class="col-md-4">
              <div>家务：{{user_life.housework}}</div>
              <div>是否与父母同住：{{user_life.parent}}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="center">
      <div class="row">
        <div class="col-md-3">
          <div class="div-orange">
            <img src="../assets/member_icon/game.svg" alt="">
          </div>
          <p class="div-name" style="margin-left: 85px;margin-top: 10px">兴趣爱好</p>
        </div>
        <div class="col-md-9">
          <div class="row center-right">
            <div class="col-md-4">
              <div>喜欢的食物：{{user_hobby.food}}</div>
              <div>喜欢的音乐：{{user_hobby.music}}</div>
            </div>
            <div class="col-md-4">
              <div>喜欢的影视剧：{{user_hobby.film}}</div>
              <div>喜欢的书：{{user_hobby.book}}</div>
            </div>
            <div class="col-md-4">
              <div>喜欢的宠物：{{user_hobby.pet}}</div>
            </div>
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
  //用户详情页
  name: 'Member',
  data() {
    return {
      userid: '',
      user_base: {},
      user_mess: {},
      user_life: {},
      user_hobby: {},
      islogin: false,
      error:false,
      tel:'',
      password:'',
      message:'',
      id:'',
      fail:false,
      success:false,
      btn2:'加好友',
      btn3:'加关注'
    }
  },
  created: function () {
    store.commit('index_change', 0);
    this.userid = this.$route.params.userid;
    this.initMember();
    this.check_login();
  },
  methods: {
    initMember: function () {
      let _this = this;
      this.axios.get('http://47.106.14.132:8000/user/getuserAll/', {
        params: {
          id: _this.userid
        }
      })
        .then(function (response) {
          _this.user_base = response.data.user_base;
          _this.user_mess = response.data.user_mess;
          _this.user_life = response.data.user_life;
          _this.user_hobby = response.data.user_hobby;
          console.log(response.data)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    sendemail: function () {
      if (this.islogin) {
        $('#messageModal').modal('show')
      } else {
        $('#myModal').modal('show');
      }
    },
    check_login: function () {
      let _this = this
      let token = localStorage.getItem('token')
      let id = localStorage.getItem('id')
      if (token) {
        this.axios.get('http://47.106.14.132:8000/user/check_login/', {
          headers: {
            'token': token
          },
          params: {
            id: id
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
    check_tel:function () {
      let reg=/^\d{11}$/;
      if (reg.test(this.tel)) {
        return true
      }else {
        return false
      }
    },
    check_pwd:function () {
      let reg=/^\w{6,16}$/;
      if (reg.test(this.password)) {
        return true
      }else {
        return false
      }
    },
    //  登录
    login_in:function () {
      let _this=this;
      if (this.check_tel() && this.check_pwd()){
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
              _this.islogin=true;
              store.commit('login_in',response['id'])
              $('#myModal').modal('hide');
              _this.error=false
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
    //发送消息
    seedmessage:function () {
      let _this=this
      if (this.message){
        _this.id=localStorage.getItem('id')
        this.axios.get('http://47.106.14.132:8000/message/addmessage/',{
          params:{
            senduser:_this.id,
            receiveuser:_this.userid,
            message:_this.message
          }
        })
          .then(function (response) {
            console.log(response.data)
            if(response.data.id){
              _this.success=true
              _this.fail=false
              _this.message=''
            }else {
              _this.success=false
              _this.fail=true
            }
          })
          .catch(function (error) {
            console.log(error)
            _this.success=false
            _this.fail=true
          })
      }
    },
  //  加好友
    addfriend: function () {
      if (this.islogin) {
        if (this.btn2=='加好友'){
          let _this=this;
          this.id=localStorage.getItem('id')
          this.axios.get('http://47.106.14.132:8000/user/addfriend/',{
            params:{
              sendid:_this.id,
              receiveid:_this.userid
            }
          })
            .then(function (response) {
              console.log(response.data)
              if (response.data.id){
                _this.btn2='请求已发送'
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        }
      } else {
        $('#myModal').modal('show');
      }
    },
  //  加关注
    like:function () {
      if (this.islogin) {
        if (this.btn3=='加关注'){
          let _this=this;
          this.id=localStorage.getItem('id')
          this.axios.get('http://47.106.14.132:8000/user/addfollow/',{
            params:{
              liking:_this.id,
              liked:_this.userid
            }
          })
            .then(function (response) {
              console.log(response.data)
              if (response.data.id){
                _this.btn3='已关注'
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        } else {
          let _this=this
          this.id=localStorage.getItem('id')
          this.axios.get('http://47.106.14.132:8000/user/delfollow/',{
            params:{
              liking:_this.id,
              liked:_this.userid
            }
          })
            .then(function (response) {
              console.log(response.data)
              if (response.data.id){
                _this.btn3='加关注'
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        }
      } else {
        $('#myModal').modal('show');
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body,ul,li,table,div,a,input{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  a{
    color: white;
    text-decoration: none;
  }
  a:hover{
    text-decoration: solid underline white;
  }

  li{
    list-style: none;
    background: rgba(255,0,0,0);
    float: left;
  }
  .container{
    margin: auto;
  }
  .left{
    width: 100%;
    margin-top: 20px;
    height: 360px;
  }
  .right{
    margin-top: 40px;
    padding-left: 40px;
  }
  .div-name{
    font-size: 1.5em;
    color: #DD5092;
    font-weight: bolder;
    letter-spacing: 2px;
  }
  .div-id{
    font-size: 1.2em;
  }
  .div-line{
    width: 90%;
    border-bottom: 1px dashed lightblue;
  }
  .under{
    margin-top: 100px;
  }
  .div-col{
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .title{
    font-size: 1.5em;
  }

  .mybtn{
    width: 185px;
    height: 40px;
    margin-top: 20px;
    border: none;
    font-size: 1.2em;
    margin-right: 20px;
  }
  .center{
    margin-top: 20px;
    width: 100%;
    border-top: solid lightblue 1px;
    height: 227px;
  }
  .div-orange{
    background: #DD5092;
    width: 90px;
    height: 90px;
    border-radius: 50%;
    margin: auto;
    margin-top: 50px;
    padding-left: 15px;
    padding-top: 15px;
  }
  .center-right{
    margin-top: 20px;
  }
  .center-right div{
    margin-top: 20px;
  }
  #myModal .modal-dialog {
    width: 400px;
    height: 100%;
    top: 35%;
    left: 35%;
    text-align: center;
  }
  #myModal .modal-content>div{
    margin: 20px 20px 10px 20px;
  }

  #myModal input{
    margin-top: 10px;
  }
  #myModal .modal-footer{
    margin-top: 20px;
  }
  #error{
    margin-top: 10px;
    font-size: small;
    color: rgba(211, 0, 0, 0.9);
  }
  #messageModal .modal-content>div{
    margin: 20px 20px 10px 20px;
  }
  #messageModal .modal-dialog {
    width: 600px;
    height: 100%;
    padding-left: 10px;
    padding-right: 10px;
    top: 35%;
    left: 35%;
  }
  #messageModal p{
    text-align: center;
    margin-top: 10px;
    font-size: small;
  }
</style>
