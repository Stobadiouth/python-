<template>
  <div>
    <div class="row a">
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==1}">
        <a href="#" @click="chang($event)"  id="1" @mouseover="img01" @mouseout="img02"><img :src="color" alt="">最近访问</a>
      </div>
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==2}">
        <a href="#" @click="chang($event)" id="2" @mouseover="img03" @mouseout="img04"><img :src="color01" alt="">我的关注</a>
      </div>
    </div>
    <div class="col-md-12">

      <div v-if="b==1">
        <div class="row">
          <div class="col-md-2 e" >
            <a href="#" @click="c=1" :class="{bj:c==1}" >谁看过我</a>
          </div>
          <div class="col-md-2 e">
            <a href="#" @click="c=2" :class="{bj:c==2}" >我看过谁</a>
          </div>
        </div>
        <div v-if="c==1">
            <div>有<span v-text="m"></span> 位会员访问过您的主页，表示喜欢您，开通玫瑰会员，尊享全站更多项特权。<a href="#" @click="myf">立即开通>></a></div>
            <div class="row as">
              <div class="col-md-2">
                <img src="../assets/personal/25.jpg" class="img-thumbnail">
                <div class="but01">查看资料</div>
              </div>

            </div>
        </div>
        <div v-else-if="c==2">
          <div>您访问过<span v-text="n"></span> 位会员的主页，主动出击才会第一时间遇见一生有缘人！</div>
          <div class="row as">
            <div class="col-md-2">
              <img src="../assets/personal/25.jpg" class="img-thumbnail">
              <div class="but01">查看资料</div>
            </div>

          </div>
        </div>
      </div>
      <div v-else-if="b==2">
        <div class="row">
          <div class="col-md-2 e" >
            <a href="#" @click="g=1" :class="{bj:g==1}" >谁关注我</a>
          </div>
          <div class="col-md-2 e">
            <a href="#" @click="g=2" :class="{bj:g==2}" >我关注谁</a>
          </div>
        </div>
        <div v-if="g==1">
          <div>有<span v-text="t"></span> 位异性会员关注了您，开通玫瑰会员，尊享全站更多项特权。<a href="#" @click="myf">立即开通>></a></div>
          <div class="row as">
            <div class="col-md-2" v-for="i of img001">
              <img :src=i.following__img_src class="img-thumbnail">
              <router-link :to="{name:'member',params:{userid:i.following}}"><div class="but01" :name=i.following>查看资料</div></router-link>
            </div>

          </div>
        </div>
        <div v-else-if="g==2">
          <div>您关注了<span v-text="q"></span> 位异性会员，快去看看心仪的她最近都在做些什么吧！</div>
          <div class="row as">
            <div class="col-md-2" v-for="i of img002">
              <img :src=i.followed__img_src class="img-thumbnail">
              <router-link :to="{name:'member',params:{userid:i.followed}}"><div class="but01" :name=i.followed>查看资料</div></router-link>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import axios from 'axios';
  import 等待 from '../assets/personal/等待.png'
  import 等待颜色 from '../assets/personal/等待颜色.png'
  import 关注 from '../assets/personal/关注.png'
  import 关注颜色 from '../assets/personal/关注颜色.png'
  export default {
    name: 'Seeme',
    props:{
      t:'',
      q:'',
      img001:'',
      img002:'',
    },
    data() {
      return {
        c:"1",
        b: "1",
        color:等待颜色,
        color01:关注,
        m:12,
        n:5,
        g:"1",

      }
    },
    methods: {
      change:function (event) {
        this.b=event.target.id;
        alert(event.target.id)
      },
      img01:function () {
        this.color=等待颜色
      },
      img02:function () {
        if (this.b!=1){
          this.color=等待
        }
      },
      img03:function () {
        this.color01=关注颜色
      },
      img04:function () {
        if (this.b!=2){
          this.color01=关注
        }
      },
      chang:function (event) {
        this.b=event.target.id;
        if (this.b==1){
          this.color=等待颜色;
          this.color01=关注
        }else{
          this.color=等待;
          this.color01=关注颜色
        }
      },
      myf:function () {
        let s=2;
        this.$emit('memb',s)
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  a {
    text-decoration: none;
    font-size: 16px;
  }
  a img{
    margin-right:10px;
  }

  a:link {
    color: black;
  }
  a:visited {
    color: black;
  }
  a:hover {
    text-decoration: none;
    color: orangered;
  }
  .a {
    border-bottom: solid red 1px;
  }
  .div-text:hover{
    border-bottom: solid 3px #F23A6E;
  }
  .div-text {
    height: 100%;
    line-height: 55px;
    margin-left: 10px;
    text-align: center;
  }
  .border {
    height: 100%;
    text-align: center;
    line-height: 55px;
    border-bottom: solid 3px #F23A6E;
  }
  .e{
    margin-top: 20px;
  }
a.bj{
  color: orangered;
}
.as{
  margin-top: 20px;
}
.but01{
  width:130px;
  height:30px;
  background: #FF6600;
  text-align: center;
  line-height: 30px;
  color:white;
}
  .but01:hover{
    background: orangered;
    cursor: pointer;
  }
</style>
