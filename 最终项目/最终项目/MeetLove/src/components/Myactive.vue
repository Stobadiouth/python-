<template>
  <div class="row">
    <div class="col-md-4" v-for="i in list" style="margin-top: 20px" v-show="flag">
      <div class="thumbnail" style="height: 380px">
        <div style="height: 310px;width: 100%">
          <img :src="i.active__img_src" style="width:100% ;height: 220px">
          <h3 v-text="i.active__title"></h3><br/>
        </div>
        <div>
          <img src="../assets/activity/time.png" height="25" width="25" style="margin-left: 10px;display: inline;margin-bottom: 10px"/><span v-text="i.active__date"></span><br/>
          <img src="../assets/activity/person.png" height="25" width="25" style="margin-left:10px;display: inline;margin-bottom: 10px"/><span v-text="'已报名'+i.active__number+'人'" style=""></span>
        </div>
      </div>
      <div>
        <router-link to='/activemess'><button class="btn" role="button" >查看详情</button></router-link>
      </div>
    </div>
   <div class="row">
     <div class="col-md-2" v-show="!flag">
       <img src="../assets/personal/活动.png" style="margin-top: 50px;margin-left: 50px">
     </div>
     <div class="col-md-8 d">
       <div>您还没有报名任何活动哦，快去看看都有什么活动吧，<br>心仪的TA在等着你呢！<router-link to="/active"><a href="#" class="aa">查看活动>></a></router-link></div>
     </div>
   </div>
  </div>

</template>

<script>
  import axios from 'axios';

  export default {
    name: 'myactive',
    data () {
      return {
        flag:true,
        list: [],
      }
    },
    mounted:function () {
      this.getmyactivity();
    },
    methods: {
      getmyactivity:function () {
        let id=localStorage.getItem('id');
        let params = new URLSearchParams();
        let vm=this;
        params.append('id', id);
        axios.post('http://47.106.14.132:8000/activity/getmyactivity/',params)
          .then(function (response) {
            if (response.data.length) {
              vm.list=response.data;
            }else {
             vm.flag=false
            }

          })
      },
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .btn{
    margin-top:-15px;
    color:palevioletred;
    background: pink;
    width:100px;
    height: 40px;
  }
.btn:hover{
  color:white;
  background: #ffa0a5;
}
  .d {
    margin-left: 20px;
    margin-top:80px;
    color: #666666;
    font-size: 17px;
  }
.aa{
  color: orangered;
}
  .aa:hover{
    text-decoration: none;
  }
</style>
