<template>
  <div class="container">
    <div class="row">
    <div class="col-md-4" v-for="i in list">
      <div class="thumbnail" >
        <router-link to='/activemess'><a href="#"><img :src="i.img_src" style="width:350px ;height: 220px"></a></router-link>
        <div class="caption" style="height: 300px;position: relative">
          <h3 v-text="i.title"></h3><br/>
          <img src="../assets/activity/time.png" height="32" width="32"/>
          <span v-text="i.date"></span><br/>
          <img src="../assets/activity/index.png" height="32" width="32"/>
          <span v-text="i.addr"></span><br/>
          <img src="../assets/activity/person.png" height="32" width="32"/>
          <span v-text="'已报名'+i.number+'人'"></span><br/>
          <button class="btn btn-primary" role="button" style="color:palevioletred;background: pink;width: 300px;height: 40px;position: absolute;top:240px;left: 20px" @click.stop="join(i.id)">我要报名</button><br/>
        </div>
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
    <nav aria-label="Page navigation" style="width: 300px;margin: auto;padding-top: 30px ">
      <ul class="pagination">
        <li>
          <a href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
          </a>
        </li>
        <li @click="index=1"><a href="">1</a></li>
        <li @click="index=2"><a>2</a></li>
        <li @click="index=3"><a href="">3</a></li>
        <li @click="index=4"><a href="">4</a></li>
        <li @click="index=5"><a href="">5</a></li>
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
  import $ from 'jquery'
  window.$ = $;
  window.jQuery = $;
  import 'bootstrap/js/modal'

  export default {
    name: 'Fw',
    data () {
      return {
        index: "1",
        list: [],
        tel:'',
        password:'',
        userid:'',
        islogin:false,
        error:false
      }
    },
    mounted:function () {
      store.commit('index_change', 5);
      this.getactivity();
      this.check_login()
    },
    methods: {
      getactivity:function () {
          let _this=this
          this.axios.get('http://47.106.14.132:8000/activity/getacivity/',{
            params:{
              index:_this.index
            }
          })
            .then(function (response) {
              _this.list = response.data;
              console.log(response.data);
            })
            .catch(function (error) {
              console.log(error)
            })
        },
      join:function (i) {
        let _this=this
        this.userid=localStorage.getItem('id');
        if (this.islogin) {
          this.axios.get('http://47.106.14.132:8000/activity/joinactive/',{
            params:{
              id:i,
              userid:this.userid
            }
          })
            .then(function (response) {
              console.log(response.data);
              if (response.data.code=='202'){
                alert('报名成功')
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        }else {
          $('#myModal').modal('show');
        }
      },
      check_login: function () {
        let _this = this
        let token = localStorage.getItem('token')
        this.userid = localStorage.getItem('id')
        if (token) {
          this.axios.get('http://47.106.14.132:8000/user/check_login/', {
            headers: {
              'token': token
            },
            params: {
              id: _this.userid
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
                $('#myModal').modal('hide');
                store.commit('login_in',response['id'])
                _this.islogin=true
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
    }
  }
</script>

<style scoped>
  .container{
    padding-top: 40px;
    margin: auto;
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
</style>

