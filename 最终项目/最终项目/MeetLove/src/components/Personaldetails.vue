<template>
  <div>
    <div class="row">
      <!--页面提示语-->
      <div class="col-md-12  a">
        <div><img src="../assets/personal/开心.png"></div>
        <div>填写完整的详细资料才能让喜欢你的人更容易的找到你，资料越详细越容易促使对方有交往下去的意愿，
          <br/>完善详细资料您的资料完整度会增加哦！
        </div>
      </div>
    </div>
    <div class="div01">个人及工作状况</div>
    <div class="row">
      <div>
        <div class="hukou col-md-6" v-for="(v,k) in messages">
          <span v-text="k+'：'">:</span>
          <xialakuang :message="v" :key01="k" @mes="mess" :valu="messagedetail"></xialakuang>
        </div>
        <div class="hukou col-md-6" v-for="(v,k) in weight01">
          <span v-text="k+'：'">:</span>
          <xialakuang :message="v" :key01="k" @mes="mess" :valu="messagedetail"></xialakuang>
        </div>
        <div class="hukou col-md-6">
          <span>你的户口：</span>
          <wangsong @prov01="updatemessage"></wangsong>
        </div>
        <div class="hukou col-md-6">
          <span>你的学校：</span>
          <xuexiao @xuexiao="xuexiao01"></xuexiao>
        </div>
      </div>
    </div>
    <div class="div01 b">家庭状态&&爱情规划</div>
    <div class="row col-md-6" v-for="(v,k) in loves">
      <div class="row lov">
        <div class="col-md-4" >
          <span v-text="k+'：'">:</span>
        </div>
        <div class="col-md-7">
          <xialakuang :message="v" :key01="k" @mes="mess" :valu="messagedetail"></xialakuang></div>
      </div>
    </div>
    <div v-text="tishi04" style="color: red;font-size: 20px;font-weight: bolder;margin-left: 380px;margin-top: 50px"></div>
    <button class="btn" @click="savemessage($event)">保存</button>
  </div>
</template>
<script>
  import axios from 'axios';
  import $ from 'jquery';
  export default {
    name: 'Personaldetails',
    data() {
      return {
        tishi04:'',
        weight01: {},
        messages: {
          "是否吸烟": [ '请选择', '不吸烟', '稍微抽一点', '只在社交场合抽', '抽的很多'],
          "是否购车": [ '请选择', '暂无购车计划', '目前已有购车计划','已购车'],
          "你的血型": ['请选择', 'A型', 'B型', 'AB型', 'O型', '其他'],
          "你的民族": ['请选择', '汉族', '朝鲜族', '维吾尔族', '满族', '其他'],
          "是否喝酒": ['请选择', '不喝酒', '稍微喝一点', '只在社交场合喝', '喝的很多'],
          "你的体型": [ '请选择', '很瘦', '较瘦', '苗条', '匀称', '高挑', '丰满', '健壮', '较胖', '胖'],
          "住房条件": ['请选择', '和家人同住', '已购房', '租房', '打算婚后购房', '单位宿舍'],
          "宗教信仰": ['请选择', '无神论', '佛教', '道教', '基督教', '天主教', '儒教', '犹太教', '回教', '伊斯兰教', '印度教', '信神，但未定教', '其他'],
          "生活作息": [ '请选择', '早睡早起', '偶尔熬夜', '经常熬夜', '偶尔懒散', '没有规律'],
          "你的星座": [ '请选择', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座'],
          "公司性质": ['请选择',  '政府机关', '事业单位', '外企企业', '世界500强', '上市公司', '国有企业', '私营企业', '自有公司'],
          "公司行业": [ '请选择', '销售', '客户服务', '计算机/互联网', '通信/电子', '生产/制造', '物流/仓储', '商贸/采购', '人事/行政', '高级管理', '广告/市场', '传媒/艺术', '生物/制药', '医疗/护理', '金融/银行/保险', '建筑/房地产', '邮电通信',
                        '咨询/顾问', '法律', '财会/审计', '教育/科研', '服务业', '交通运输', '政府机构', '军人/警察', '自由职业', '在校学生', '待业', '其他行业', '农林牧渔', '退休'],
          "工作状态": [ '请选择','轻松稳定', '朝九晚五', '偶尔加班', '经常加班', '偶尔出差', '经常出差', '常有应酬', '工作时间自由'],
        },
        loves: {
          "家中排行": ['请选择', '独生子女', '老大', '老二', '老三', '老四', '老五', '老六', '其他'],
          "父母经济": ['请选择', '以后告诉你', '均有退休金', '均无退休金', '只有父亲有退休金', '只有母亲有退休金'],
          "厨艺状况": ['请选择', '色香味俱全', '能做几样可口的小菜', '有待提高'],
          "家务": ['请选择', '愿承担大部分家务', '希望对方承担大部分家务', '看各自忙闲，协商分担家务'],
          "有无子女": ['请选择', '没有', '有，我们住在一起', '有，我们偶尔一起住', '有，但不在身边'],
          "何时结婚": ['请选择', '及时闪婚', '一年以内', '两年以内', '三年以内', '时机成熟时就结婚'],
          "父母情况": ['请选择', '父母健在', '单亲家庭', '父亲健在', '母亲健在', '父母均离世'],
          "是否想要小孩": ['请选择', '想', '不想', '还没想好', '视情况而定'],
          "偏爱的约会方式": ['请选择', '一起打游戏或者看电影', '一起做饭', '一起旅游', '散步', '相互依偎'],
          "愿与对方父母同住": ['请选择', '与自己父母同住', '不与自己父母同住', '尊重伴侣意见','视具体情况而定'],
        },
        school:'',
        messagedetail:{},

      }
    },
    mounted: function () {
      this.zengweight();
      this.getusemessage()
    },
    methods: {
      getusemessage:function(){
        let vm=this;
        let id=localStorage.getItem('id');
        axios.get('http://47.106.14.132:8000/user/getuserAll/',{
          params:{id:id}
        })
          .then(function (response) {
            let a=response.data["user_life"];
            let b=response.data["user_mess"];
            vm.messagedetail={
              "是否吸烟":a["smoke"],
              "是否喝酒":a["drink"],
              "你的星座":b["constellation"],
                "是否购车":a["car"],
                "你的血型":b["blood"],
                "你的民族":b["nation"],
                "住房条件":b["house"],
                "你的体型":b["weightstyle"],
                "宗教信仰":a["faith"],
                "生活作息":a["livestyle"],
                "公司性质":b["companystyle"],
                "公司行业":b["profession"],
                "工作状态":b["jobcode"],
                "家中排行":a["familynum"],
                "父母经济":a["parentmoney"],
                "厨艺状况":a["cook"],
                "家务":a["housework"],
                "有无子女":b["children"],
                "何时结婚":a["marrytime"],
                "父母情况":a["parentcode"],
                "是否想要小孩":a["wantchild"],
                "偏爱的约会方式":b["engagements"],
                "你的体重":b["weight"],
                "愿与对方父母同住":a["parent"],
                "school":b["school"],
                "city":b["addr"]
            };

          })
          .catch(function (error) {
            console.log(error);
          })
      },
      xuexiao01:function(i){
        this.school=i;
      },

      zengweight:function(){
        let w=[];
        for (let i =39; i <110; i++) {
          if(i==39){
            w.push("请选择")
          }else{
            w.push(i+'公斤')
          }this.weight01={"你的体重":w}
        }

      },
      savemessage:function () {
        this.messagedetail["school"]=this.school;
        let id=localStorage.getItem('id');
        let a=this.messagedetail;
        let vm=this;
        let meaa={
          "id":id,
          "smoke":a["是否吸烟"],
          "drink":a["是否喝酒"],
          "constellation":a["你的星座"],
          "car":a["是否购车"],
          "blood":a["你的血型"],
          "nation":a["你的民族"],
          "house":a["住房条件"],
          "weightstyle":a["你的体型"],
          "faith":a["宗教信仰"],
          "livestyle":a["生活作息"],
          "companystyle":a["公司性质"],
          "profession":a["公司行业"],
          "jobcode":a["工作状态"],
          "familynum":a["家中排行"],
          "parentmoney":a["父母经济"],
          "cook":a["厨艺状况"],
          "housework":a["家务"],
          "children":a["有无子女"],
          "marrytime":a["何时结婚"],
          "parentcode":a["父母情况"],
          "wantchild":a["是否想要小孩"],
          "engagements":a["偏爱的约会方式"],
          "weight":a["你的体重"],
          "parent":a["愿与对方父母同住"],
          "school":a["school"],
          "addr":a["city"]
        };
        $.ajax(
                {
                    url:'http://47.106.14.132:8000/user/changedetailmessage/',
                    type:"POST",
                    data:JSON.stringify(meaa),
                    dataType:"json",
                    contentType:"application/json",
                    success:function (response,textStatus,xhr) {
                      vm.tishi04='保存成功！';
                      setTimeout(function () {
                        vm.tishi04='';
                        vm.makesure=0
                      },2000)

                    },
                    error:function (XMLHttpRequest,textStatus,errorThrown) {
                      vm.tishi04='保存失败！';
                      setTimeout(function () {
                        vm.tishi04='';
                        vm.makesure=0
                      },2000)
                    }
                }
            )
      },
      updatemessage:function (a) {
        this.messagedetail["city"]=a
      },
      mess:function (e) {
        this.messagedetail[e[0]]=e[1];
      }
    }
  }

</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body, ul, li, table, div, a, input {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
  }

  .a {
    color: #BDBDBD;
    margin-left: 100px;
    margin-top: 10px;
    display: flex;
  }
  .b{
    padding-top:50px;
  }

  .hukou {
    display: flex;
    line-height: 2.5em;
    margin-top: 20px;
  }

  .div01 {
    color: #0e0e0e;
    font-size: 17px;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .lov {
    line-height: 2.5em;
    padding-top: 20px;
  }
  .lov div span{
    /*padding-left:28px;*/
  }

  div span {
    color: #BDBDBD;
  }

  .btn {
    position:relative;
    width: 80px;
    height: 50px;
    background: rgba(180, 3, 3, 0.8);
    color: white;
    margin-top: 50px;
    margin-left: 400px;
  }
</style>
