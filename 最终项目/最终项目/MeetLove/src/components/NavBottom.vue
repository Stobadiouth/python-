<template>
  <div class="container-fluid bottom">
    <div class="container">
      <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-3">
          <p>简介</p>
          <router-link to="/about"><a href=""><p>关于我们</p></a></router-link>
          <a href=""><p>服务声明</p></a>
          <a href=""><p>媒体报道</p></a>
        </div>
        <div class="col-md-3">
          <p>合作</p>
          <a href=""><p>加入我们</p></a>
          <a href=""><p>联系我们</p></a>
          <a href=""><p>友情链接</p></a>
        </div>
        <div class="col-md-3">
          <p>帮助</p>
          <a href=""><p>帮助中心</p></a>
          <a href=""><p>常见问题</p></a>
          <a href=""><p>新手引导</p></a>
        </div>
        <div class="col-md-1"></div>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .bottom{
    width: 100%;
    height: 140px;
    background: url("../assets/index/flower.png");
    /*background-position: 600px 200px;*/
    margin-top: 100px;
  }
  .bottom div{
    font-size: 0.8em;
    text-align: center;
  }
  .bottom>div a{
    color: grey;
  }
  .bottom>div a:hover{
    color: orangered;
    text-decoration: none;
  }

</style>
