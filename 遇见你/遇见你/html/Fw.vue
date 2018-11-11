<template>
  <div class="row">
      <div href="#" class="col-sm-6 col-md-4" v-for="i in list" >
        <div class="thumbnail" >
          <router-link to='/hdxq'><a href="#"><img :src="i.src"></a></router-link>
          <div class="caption">
            <span v-text="i.name"></span><br/>
              <img src="../../../123/src/assets/time.png" height="32" width="32"/>
            <span v-text="i.date"></span><br/>
              <img src="../../../123/src/assets/index.png" height="32" width="32"/>
            <span v-text="i.direct"></span><br/>
              <img src="../../../123/src/assets/person.png" height="32" width="32"/>
            <span v-text="i.person"></span><br/>
            <a href="#" class="btn btn-primary" role="button" style="margin-left: 20px;color:palevioletred;background: pink;width: 300px;height: 40px;margin-top: auto" @click.prevent="baoming">我要报名</a><br/>
          </div>
        </div>
      </div>

    <nav style="text-align: center">
      <ul class="pager" >
        <li><a href="#">1</a></li>
        <li><a href="#">2</a></li>
        <li><a href="#">3</a></li>
        <li><a href="#">4</a></li>
        <li><a href="#">5</a></li>
        <li><a href="#">6</a></li>
        <li><a href="#">7</a></li>
        <li><a href="#">8</a></li>
        <li><a href="#">9</a></li>
        <li><a href="#">10</a></li>
        <li><a href="#">下一页</a></li>
        <li><a href="#">最后一页</a></li>
      </ul>
    </nav>

    <div class="row2">
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">
        <strong>关于我们</strong><br>
        <router-link to='/about'><a href="#">关于我们</a></router-link>
        <router-link to='/about'><a href="#">关于我们</a><br></router-link>
        <router-link to='/about'><a href="#">关于我们</a></router-link>
        <router-link to='/about'><a href="#">关于我们</a><br></router-link>
        <router-link to='/about'><a href="#">关于我们</a></router-link>
        <router-link to='/about'><a href="#">关于我们</a><br></router-link>
      </div>
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">手机微信</div>

      <!-- Add the extra clearfix for only the required viewport -->
      <div class="clearfix visible-xs-block">
      </div>

      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">
        <strong>服务热线</strong><br>
        热线电话：0571-85337299
        <br>地址：杭州市朝晖路219号中山花园写字楼3楼 ( 地铁1号线西湖文化广场站，附近公交 车站：西湖文化广场，中北桥
      </div>
      <div class="col-xs-6 col-sm-3" style="border-right: solid 1px grey;height: 80px;text-align: center">友情链接<br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br>
        <a href="#">关于我们</a>
        <a href="#">关于我们</a><br></div>
    </div>

  </div>
</template>

<script>

  export default {
    name: 'Fw',
    data () {
      return {
        b: "1",
        list:[{"name":"2018年相亲大会","date":"10月27日","direct":"国际宴会中心","person":"已报名43人","src":"http://www.hongniang.com/data/upload/event/20180814/5b723cdd2caba.jpg"},
            {"name":"","date":"10.28","direct":"指尖互动，不受地点限制","person":"已报名23人","src":"http://www.hongniang.com/data/upload/event/20170918/59bf38d8abb60.png"},
            {"name":"","date":"10.27","direct":"指尖互动，不受地点限制","person":"已报名2人","src":"http://www.hongniang.com/data/upload/event/20180907/5b91e4bfd0af3.jpg"},
            {"name":"","date":"10.27","direct":"指尖互动，不受地点限制","person":"已报名2人","src":"http://www.hongniang.com/data/upload/event/20170601/592fd5a8deab4.jpg"},
            {"name":"","date":"10.27","direct":"指尖互动，不受地点限制","person":"已报名2人","src":"http://www.hongniang.com/data/upload/event/20170619/59477fcf909ab.jpg"},
            {"name":"","date":"10.27","direct":"指尖互动，不受地点限制","person":"已报名2人","src":"http://www.hongniang.com/data/upload/event/20170609/5939ed6aba8fb.jpg"}],

      }


    },
    mounted:function () {
      this.getdata()
    },

    methods: {
      jump(){
        //this.$router.push("/cart")
        //传递的参数用{{ $route.query.goodsId }}获取
        this.$router.push({name:'hdxq'})
        //this.$router.go(-2)
        //后退两步
      },
      getdata:function () {
        var vm = this;
        axios({
          // url:http://course/getcoursebytypeid/'+this.type_id+'/'
          url: 'http://localhost:8000/actiity/getactivity/',


        }).then(function (response) {
          console.log(response.data)
          vm.list = response.data

          console.log(vm.list)
        })
          .catch(function (error) {
            console.log(error)
          })
      },
      baoming:function () {
        var vm = this;
        axios({
          // url:http://course/getcoursebytypeid/'+this.type_id+'/'
          url: 'http://localhost:8000/actiity/baoming/',


        }).then(function (response) {
          console.log(response.data)
          vm.list = response.data

          console.log(vm.list)
        })
          .catch(function (error) {
            console.log(error)
          })
      }
    }


  }
</script>

<style scoped>
.huodong{
  border: 1px solid black;
}

</style>
