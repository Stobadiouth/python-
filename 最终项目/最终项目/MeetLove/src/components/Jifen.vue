<template>
  <div class="tou">
    <div class="min">
      <div>欢迎您，<span v-text="m"></span></div>
      <div>我的积分：<span v-text="q+'积分'" class="jinbi"></span>花费玫瑰金币可以提升您的积分哦！</div>
    </div>
    <div class="nav nav-tabs aa">
          <div class="he">
            <span class="b">积分值：
              <span v-text="q+'积分'"></span>
            </span>
          </div>
        <div style="width:500px;margin-left: 150px;margin-top:30px">
          <div class="progress">
            <div class="progress-bar progress-bar-warning progress-bar-striped " role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" :style="{width:persent}">
                    <span v-text="persent"></span>
            </div>
          </div>
          <div>距离下一等级还有
            <span v-text="cha" style="color: red;"></span>积分</div>
        </div>

    </div>
    <div class="dixia">
      <div><img src="../assets/personal/玫瑰.png" alt="" style="margin-top:-10px;margin-right: 5px"><h5 style="display: inline">
        关于积分</h5></div>
      <div class="l01"></div>
      <div>
        <ul style="margin-top:20px;margin-left: 20px;color: red">
          <li><span style="color: #666666">每花费1玫瑰金币会增加1积分值，积分随着玫瑰金币的花销逐渐增加。</span></li>
          <li><span style="color: #666666">积分可以在商城购买专属礼物，线上、线下礼物均可以通过积分进行兑换。</span></li>
          <li><span style="color: #666666">积分属于虚拟货币，不可退费，同时我们还提供了多种功能，方便您消费及使用剩余的积分。</span></li>
          <li><span style="color: #666666">活动最终解释权归遇见爱所有。</span></li>
          <li><span style="color: #666666">积分将于在线支付玫瑰金币成功后自动增加。</span></li>
          <li><span style="color: #666666">对服务有任何疑问或出现使用问题，请咨询客服专线 877476153（8：00 至 20：00） 咨询。</span></li>
          <li><span style="color: #666666">积分不予体现，敬请谅解。</span></li>
        </ul>
      </div>
      <div style="margin-top:50px"><img src="../assets/personal/说明.png" alt="" style="margin-top:-10px;margin-right: 5px"><h5
        style="display: inline">积分等级</h5></div>
      <div class="l01"></div>
      <div>
        <ul style="margin-top:20px;margin-left: 20px;color: red">
          <li><span style="color: #666666">一级：1000积分。</span></li>
          <li><span style="color: #666666">二级：1500积分。</span></li>
          <li><span style="color: #666666">三级：2000积分。</span></li>
          <li><span style="color: #666666">四级：2500积分。</span></li>
          <li><span style="color: #666666">五级：3000积分。</span></li>
          <li><span style="color: #666666">六级：10000积分。</span></li>
          <li><span style="color: #666666">至尊：20000积分。</span></li>
        </ul>
      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: 'Jifen',
    props:{
      q: '',
      m: '',
    },
    data() {
      return {
        ji:1500,
        cha:21,
        persent: '30%',
        b: 1,
        jinbi01: [15, 20, 50, 150, 300, 500],
        shuliang: 15,
        jin: 30,
        op: 15
      }
    },
    mounted:function(){
      this.jisuan()
    },
    methods: {
      jisuan:function () {
        this.cha=this.ji-this.q;
        let op=(this.q/this.ji)*100;
        this.persent=op.toFixed(2)+'%'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .tou {
    width: 100%;
    height: 800px;
    /*border: solid red 1px;*/
  }

  .min {
    margin-top: 50px;
    padding-left: 20px;
    margin-bottom: 50px;
  }

  .jinbi {
    margin-right: 20px;
    color: red;
  }
  .he{
    margin-top: 20px;
  }
  .b {
    font-size: 15px;
    color:#0e0e0e;
    padding-left:50px;
  }

  .b span {
    color: #FF6600;
    font-size: 20px;
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

  .aa {
    height: 200px;
    border-left: solid #F23A6E 1px;
    border-right: solid #F23A6E 1px;
    border-top: solid #F23A6E 1px;
    background: #ffd1de;
  }

  .dixia {
    margin-top: 50px;
  }

  .l01 {
    width: 100%;
    height: 1px;
    background: #F23A6E;
  }
</style>
