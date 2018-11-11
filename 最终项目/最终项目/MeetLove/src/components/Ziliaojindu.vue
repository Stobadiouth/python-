<template>
  <div>
    <div class="row a">
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==1}">
        <a href="#" @click="b=1" id="1" >基本资料</a>
      </div>
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==2}">
        <a href="#" @click="b=2" >我的照片</a>
      </div>
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==3}">
        <a href="#" @click="b=3" >个人宣言</a>
      </div>
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==4}">
        <a href="#" @click="b=4" >详细资料</a>
      </div>
      <div class="div-text col-md-2 col-sm-1" :class="{border:b==5}">
        <a href="#" @click.prevent="b=5" >个人喜好</a>
      </div>
    </div>
    <div class="col-md-12">

      <div v-if="b==1">
        <perziliao @namechange="namechange01"></perziliao>
      </div>
      <div v-else-if="b==2">
        <photo @pic="pic01"></photo>
      </div>
      <div v-else-if="b==3">
        <gerenxuanyan></gerenxuanyan>
      </div>
      <div v-else-if="b==4">
        <personaldetails ></personaldetails>
      </div>
      <div v-else>
        <hobby></hobby>
      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: 'Ziliaojindu',
    data() {
      return {
        c:"1",
        b: "1",
      }
    },
    methods: {
      change:function (event) {
        this.b=event.target.id;
        alert(event.target.id)
      },
      pic01:function (i) {
        this.$emit('pic02',i)
      },
      namechange01:function(i){
        this.$emit('namechange02',i)
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


</style>
