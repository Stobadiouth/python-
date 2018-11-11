<template>
  <div>
    <div class="row">
      <div class="col-md-5 a">我的资料</div>
      <div class="col-md-2"><span class="b">资料完整度：<span v-text="persent"></span></span></div>
      <div class="col-md-5">
        <div class="progress">
          <div class="progress-bar progress-bar-warning c" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" :style='{width:persent}'></div>
        </div>
      </div>
    </div>
    <ziliaojindu @pic02="pic03" @namechange02="namechange03"></ziliaojindu>
  </div>
</template>

<script>
  import axios from 'axios';
export default {
  name: 'Material',
  data () {
    return {
      persent:'30%',
      q:'',
      m:'',
    }
  },
  mounted: function () {
    this.getpersent()

  },
  methods:{
    getpersent:function(){
      let params = new URLSearchParams();
      let id=localStorage.getItem('id');
      params.append('id', id);
      let vm=this;

      axios.post('http://47.106.14.132:8000/search/persent/',params)
        .then(function (response) {
          vm.count(response.data['message'][0]);
          vm.count(response.data['base'][0]);
          vm.count(response.data['life'][0]);
          vm.count(response.data['hobby'][0]);
          vm.count01(response.data['photo'][0]);
          vm.count01(response.data['signture'][0]);
          console.log(response.data['signture'][0]);

          // for (let i in response.data['base'][0]){
          //   if (response.data['base'][0][i]){
          //     q++
          //   }
          // }
          // for (let i in response.data['life'][0]){
          //   if (response.data['life'][0][i]){
          //     q++
          //   }
          // }

        });
    },
    count:function(w){
      for (let i in w){
        if (w[i]){
          this.q++
        }

      }this.q=this.q-1;
      if (this.q>35) {
        this.q=70
      }else{
        this.q=this.q*2
      }
    },
    count01:function(w){
      this.m=0;
      for (let i in w){
        if (w[i]){
          this.m++
        }

      }
      this.q=this.q+this.m*10;
      this.persent=this.q+'%'
    },
    pic03:function (i) {
      this.$emit('pic04',i)
    },
    namechange03:function (i) {
      this.$emit('namechange04',i)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .a{
    height: 30px;
    font-size:25px;
  }
  .b{
    font-size: 15px;
    color:#BDBDBD;
    padding-left:15px;
  }
  .b span{
    color: #FF6600;
    font-size:20px;
  }
  .col-md-2{
    padding: 0;
    padding-left:15px;
  }
  .row{
    padding-top: 20px;
    line-height: 16px;
  }
  .c{
    padding-top: 20px;
  }
  .progress{
  height: 16px;
  }
</style>
