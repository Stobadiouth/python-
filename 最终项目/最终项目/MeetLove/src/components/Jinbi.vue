<template>
  <div class="tou">
    <div class="min"><div>欢迎您，<span v-text="m"></span></div>
    <div>我的金币：<span v-text="q+'金币'" class="jinbi"></span>充值金币，您的财富值也会上涨哦，线上爱情也会来的更快呢！</div>
    </div>
    <ul class="nav nav-tabs">
      <li role="presentation" :class="{active:b==1}"><a href="#" @click.stop.prevent="b=1">在线支付</a></li>
      <li role="presentation" :class="{active:b==2}"><a href="#" @click.stop.prevent="b=2">15元玫瑰金币包月</a></li>
      <li role="presentation" :class="{active:b==3}"><a href="#" @click.stop.prevent="b=3">手机支付</a></li>
      <li role="presentation" :class="{active:b==4}"><a href="#" @click.stop.prevent="b=4">购买记录</a></li>
    </ul>
    <div class="nav nav-tabs aa">
      <div v-if="b==1">
        <div class="goumai">购买数量：
          <div v-for="i in jinbi01">
            <div class="meigui" :class="{meigui01:shuliang==i}" v-text="i+'金币'" @click="buy(i)"></div>
            <img src="../assets/personal/玫瑰花.png" alt="" :class="{o:shuliang==i}">
          </div>
        </div>
        <div style="margin-left:130px;margin-top:20px">您将购买<span v-text="shuliang"></span>金币，需支付<span v-text="jin" style="color: red"></span>元。</div>
        <div class="btn">立即购买</div>
      </div>
      <div v-else-if="b==2">
        <div class="goumai">购买数量：
          <div >
            <div class="meigui meigui01"  > 15金币</div>
            <img src="../assets/personal/玫瑰花.png" alt="" class="o">
          </div>
        </div>
        <div style="margin-left:130px;margin-top:20px">您将购买15金币，需支付<span v-text="15" style="color: red"></span>元，开通后每月将会获得15玫瑰金币。</div>
        <div class="btn">立即购买</div>
      </div>
      <div v-else-if="b==3">
        <div class="goumai">购买数量：
          <div >
            <div class="meigui meigui01"  > 15金币</div>
            <img src="../assets/personal/玫瑰花.png" alt="" class="o">
          </div>
        </div>
        <div style="margin-left:130px;margin-top:20px">您将购买15金币，需支付<span v-text="30" style="color: red"></span>元，仅支持移动用户。</div>
        <div class="btn">立即购买</div>
      </div>
      <div v-else-if="b==4">
        <div >
          <ul class="row uu">
            <li class="col-md-4">购买时间</li>
            <li class="col-md-4">购买数量</li>
            <li class="col-md-4">购买金额</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="dixia">
      <div><img src="../assets/personal/玫瑰.png" alt="" style="margin-top:-10px;margin-right: 5px"><h5 style="display: inline">玫瑰金币可以做什么？</h5></div>
      <div class="l01"></div>
      <div style="margin-top: 20px;margin-left: 20px" class="row">
        <img src="../assets/personal/礼物.png" alt="" class="col-md-1">
        <div style="color: #666666;font-size:15px">精美礼品</div>
        <div style="color: #666666;font-size:13px;margin-top: 10px">没有什么是礼物解决不了的。</div>
      </div>
      <div style="margin-top: 20px;margin-left: 20px" class="row">
        <img src="../assets/personal/表情.png" alt="" class="col-md-1">
        <div style="color: #666666;font-size:15px">专属表情</div>
        <div style="color: #666666;font-size:13px;margin-top: 10px">独特的专属表情，更容易吸引异性哦！</div>
      </div>
      <div style="margin-top:50px"><img src="../assets/personal/说明.png" alt="" style="margin-top:-10px;margin-right: 5px"><h5 style="display: inline">补充说明</h5></div>
      <div class="l01"></div>
      <div>
        <ul style="margin-top:20px;margin-left: 20px;color: red">
          <li><span style="color: #666666">玫瑰金币属于遇见爱用户个人专属虚拟货币，不能转让他人。</span></li>
          <li><span style="color: #666666">购买的玫瑰金币自购买之日起1年内有效。</span></li>
          <li><span style="color: #666666">玫瑰金币属于虚拟货币，不可退费，希望您根据需要酌情购买，同时我们还提供了多种功能，方便您消费及使用剩余的玫瑰金币。</span></li>
          <li><span style="color: #666666">活动最终解释权归遇见爱所有。</span></li>
          <li><span style="color: #666666">服务将于在线支付成功后自动开通。</span></li>
          <li><span style="color: #666666">对服务有任何疑问或出现使用问题，请咨询客服专线 877476153（8：00 至 20：00） 咨询。</span></li>
          <li><span style="color: #666666">服务一经开通，不予退款，敬请谅解。</span></li>
        </ul>
      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: 'Jinbi',
    props:{
      q:'',
      m:'',
    },
    data() {
      return {


        b:1,
        jinbi01:[15,20,50,150,300,500],
        shuliang:15,
        jin:30,
        op:15
      }
    },
    methods: {
      buy:function (i) {
        this.shuliang=i;
        this.jin=i*2
      }

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .tou{
    width: 100%;
    height:800px;
    /*border: solid red 1px;*/
  }
  .min{
    margin-top: 50px;
    padding-left: 20px;
    margin-bottom: 50px;
  }
  .jinbi{
    margin-right: 20px;
    color: red;
  }
  .nav-tabs > li > a:hover,
  .nav-tabs > li > a:focus {
    border-color: #F23A6E #F23A6E #F23A6E;
  }
  .nav-tabs {
    border-bottom: 1px solid #F23A6E;
  }

  .nav-tabs > .active > a,
  .nav-tabs > .active > a:focus {
    color: #F23A6E;
    cursor: default;
    background-color: #ffd1de;
    border: 1px solid #F23A6E;
    border-bottom-color: transparent;
  }
.aa{
  height: 200px;
  border-left: solid #F23A6E 1px;
  border-right: solid #F23A6E 1px;
  background:#ffd1de;
}
  .goumai{
    margin-top: 50px;
    margin-left: 50px;
    line-height: 30px;
    cursor: pointer;
    display: flex;
  }
  .meigui{
    width:80px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    margin-left: 10px;
    background: white;
  }
  .goumai img{
    float: right;
    margin-left:66px;
    margin-top: -22px;
    display: none;
  }
  .goumai .o{
    display: block;
  }
  .meigui01{
    box-sizing: border-box;
    border: solid #F23A6E 2px;
  }
  .btn{
    float: right;
    background: #f25684;
    margin-right:100px;
    margin-top:20px;
    color: #FFFFFF;
  }
  .btn:hover{
    background: #F23A6E;
  }
  .uu{
    text-align: center;
    margin-top: 10px;
    list-style: none;
  }
  .dixia{
    margin-top: 50px;
  }
  .l01{
    width:100%;
    height: 1px;
    background:#F23A6E;
  }
</style>
