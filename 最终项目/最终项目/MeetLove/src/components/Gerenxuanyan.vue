<template>
    <div class="row">
      <div class="col-md-12  a">
        <img src="../assets/personal/开心.png" >
        <span >
          恭喜你已经完成了个人宣言，资料完整度增加10%。
        </span>
      </div>
      <textarea type="text" id="oText" v-model="text01" @input="countnum" maxlength="400"></textarea>
      <div style="margin-left: 600px">还可以输入
        <span style="color: red" v-text="count02">12</span>
      个字符。</div>
      <div v-text="tishi04" style="color: red;font-size: 20px;font-weight: bolder;margin-left: 380px;padding-top:100px"></div>
      <button class="btn" @click="textbaocun">保存</button>
    </div>


</template>

<script>
  import axios from 'axios';
export default {
  name: 'Gerenxuanyan',
  data () {
    return {
      tishi04:'',
      text01:'',
      count01:400,
      count02:''
    }
  },
  mounted: function () {
    // 在开始页面时生成日期---------
    this.coun()
  },
  methods:{
    coun:function(){
      this.count02=this.count01
    },
    textbaocun:function () {
      let vm = this;
      let id = localStorage.getItem('id');
      let params = new URLSearchParams();
      params.append('id', id);
      params.append('signature', this.text01);
      axios.post('http://47.106.14.132:8000/user/gerenxuanyan/', params)
        .then(function (response) {
          if (response.data["code"]==202){
            vm.tishi04='保存成功！';
            setTimeout(function () {
              vm.tishi04='';
              vm.makesure=0
            },2000)
          }else {
            vm.tishi04='保存失败！';
            setTimeout(function () {
              vm.tishi04='';
              vm.makesure=0
            },2000)
          }

        });
    },
    countnum:function () {
      if(this.text01.length==null){
        this.count02=this.count01
      }else if(this.text01.length<201){
        this.count02=this.count01-this.text01.length
      }


    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .a{
    color: #BDBDBD;
    margin-left: 100px;
    margin-top:10px;
  }
  .btn {
    width: 80px;
    height: 50px;
    background: rgba(180, 3, 3, 0.8);
    color: white;
    margin-top: 50px;
    margin-left: 400px;
  }

  #oText {
    margin-top: 30px;
    margin-left: 50px;
    width: 816px;
    height: 300px;
    border: 1px dotted #ff0000;
  }


</style>
