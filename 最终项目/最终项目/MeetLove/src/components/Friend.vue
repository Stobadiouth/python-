<template>
  <div>
    <div class="div01"><img src="../assets/personal/爱心.png" alt="">你当前的择偶意向是：</div>
    <div class="row" style="margin-top: 25px">
      <div class="col-md-6 a01" v-for="(v,k) in yixiang ">
        <div class="col-md-1"></div>
        <div v-text="k+'：'" class="col-md-2 d" style="text-align: justify"></div>
        <div v-text="v" class="col-md-8 c"></div>
      </div>
    </div>
    <div class="div01"><img src="../assets/personal/爱心.png" alt="">修改择偶意向是：</div>
    <div class="row we">
      <div class="col-md-6">
        <form class="div-lable form-inline">年&nbsp;&nbsp;&nbsp;&nbsp;龄：
          <select class="form-control" v-model="c01">
            <option v-for="i in cou" v-text="i"></option>
          </select>
          至
          <select class="form-control" v-model="c02">
            <option v-for="i in cou" v-text="i"></option>
          </select>

        </form>
      </div>
      <form class="div-lable form-inline col-md-6">地&nbsp;&nbsp;&nbsp;&nbsp;区：
        <shengshiqu :k="zouxiang" @ddd01="addres"></shengshiqu>
      </form>
      <div class="col-md-6">
        <form class="div-lable form-inline">身&nbsp;&nbsp;&nbsp;&nbsp;高：
          <select class="form-control" v-model="h01">
            <option v-for="i in hei" v-text="i"></option>
          </select>
          至
          <select class="form-control" v-model="h02">
            <option v-for="i in hei" v-text="i"></option>
          </select> cm


        </form>
      </div>
      <div class="col-md-6">
        <form class="div-lable form-inline hukou">
          婚姻状况：
          <yixiang :language="lan" @ch01="ch03"></yixiang>
        </form>
      </div>
      <div class="col-md-6">
        <form class="div-lable form-inline">学&nbsp;&nbsp;&nbsp;&nbsp;历：
          <select class="form-control" v-model="wen">
            <option v-for=" i in wenhua['文化程度']" v-text="i"></option>
          </select>
        </form>
      </div>
      <div class="col-md-6">
        <form class="div-lable form-inline hukou">
          住房情况：
          <yixiang :language="zhufang"></yixiang>
        </form>
      </div>
      <div class="col-md-6">
        <form class="div-lable form-inline">月收入：
          <select class="form-control" v-model="yue">
            <option v-for=" i in yueshouru['月收入']" v-text="i"></option>
          </select>
        </form>
      </div>
      <div class="col-md-6">
        <form class="div-lable form-inline hukou">
          有无子女：
          <yixiang :language="zinv" @ch01="ch02"></yixiang>
        </form>
      </div>
    </div>
    <button class="btn" @click="savemessage($event)">保存</button>
  </div>


</template>
<script>
  import axios from 'axios';
  import $ from 'jquery'
  export default {
    name: 'Friend',
    data() {
      return {
        zouxiang:1,
        // v:1,
        cou: [],
        c01: '18岁',
        c02: '20岁',
        hei: [],
        h01: 155,
        h02: 170,
        wen: '请选择',
        zhu: '以后再告诉你',
        yue: '2000-5000',
        zi:[],
        mer:[],
        diqu:'',
        yixiang: {
          '年龄': '18-22岁',
          '地区': '北京北京东城区',
          '身高': '155-170',
          '婚姻状况': '不限',
          '学历': '不限',
          '住房情况': '不限',
          '月收入': '不限',
          '有无子女': '不限',
        },
        lan: [
          {id: 1, name: '不限'},
          {id: 2, name: '未婚'},
          {id: 3, name: '离异'},
          {id: 4, name: '丧偶'},
        ],
        wenhua: {"文化程度": ['请选择', '博士', '研究生', '大学本科', '大学专科', '专科学校', '中等专业学校', '技工学校', '大专', '高中', '初中', '小学', '文盲或半文盲']},
        yueshouru: {"月收入": ['不限', '<2000', '2000-5000', '5000-10000', '10000-20000', '20000-50000', '>50000']},
        zhufang: [
          {id: 5, name: '以后再告诉你'},
          {id: 6, name: '与父母同住'},
          {id: 7, name: '租房'},
          {id: 8, name: '已购房（有房贷）'},
          {id: 9, name: '已购房（无房贷）'},
          {id: 10, name: '住单位房'},
          {id: 11, name: '住亲朋家'},
          {id: 12, name: '需要时购置'},
        ],
        zinv: [
          {id: 13, name: '不限'},
          {id: 14, name: '没有'},
          {id: 15, name: '有，和我住在一起'},
          {id: 16, name: '有，有时和我住在一起'},
          {id: 17, name: '有，不和我住在一起'},
        ],
      }
    },
    mounted: function () {
      // 在开始页面时生成日期---------
      this.coun();
      this.heig();
      this.yixiang01();
    },
    methods: {
      addres:function(b){
        this.diqu=b
      },
      ch02:function(b){
        this.zi=b
      },
      ch03:function(b){
        this.mer=b
      },
      yixiang01: function () {
        let params = new URLSearchParams();
        let id = localStorage.getItem('id');
        params.append('id', id);
        let vm = this;
        axios.post('http://47.106.14.132:8000/user/getyixiang/', params)
          .then(function (response) {
            let s0 = response.data;
            console.log(s0['age']);
            if (s0['age']) {
              vm.yixiang['年龄'] = s0['age']
            }
            if (s0['addres']) {
              vm.yixiang['地区'] = s0['addres']
            }
            if (s0['height']) {
              vm.yixiang['身高'] = s0['height']
            }
            if (s0['marry']) {
              vm.yixiang['婚姻状况'] = s0['marry']
            }
            if (s0['edu']) {
              vm.yixiang['学历'] = s0['edu']
            }
            if (s0['house']) {
              vm.yixiang['住房情况'] = s0['house']
            }
            if (s0['income']) {
              vm.yixiang['月收入'] = s0['income']
            }
            if (s0['children']) {
              vm.yixiang['有无子女'] = s0['children']
            }


          });
      },
      coun: function () {
        for (let i = 18; i < 81; i++) {
          let a = i + '岁';
          this.cou.push(a)
        }
      },
      heig: function () {
        for (let i = 144; i < 212; i++) {
          if (i == 144) {
            let a = '145以下';
            this.hei.push(a)
          } else if (i == 211) {
            let a = '210以上';
            this.hei.push(a)
          } else {
            this.hei.push(i)
          }
        }
      },
      savemessage:function () {
        let id = localStorage.getItem('id');
        let yixian={
          "id":id,
          "age":this.c01.split("岁")[0]+'-'+this.c02,
          "height":this.h01+'-'+this.h02,
          "edu":this.wen,
          "income":this.yue,
          "house":this.zhu,
          "children":this.zi,
          "addres":this.diqu,
          "marry":this.mer,
        };
        console.log(yixian);
        $.ajax(
          {
            url:'http://47.106.14.132:8000/user/baocunyixiang/',
            type:"POST",
            data:JSON.stringify(yixian),
            dataType:"json",
            contentType:"application/json",
            success:function (response,textStatus,xhr) {
              console.log(response.code);
              console.log(textStatus);

            },
            error:function (XMLHttpRequest,textStatus,errorThrown) {
              console.log('NO!!!');
              console.log(textStatus);
            }
          }
        )
        console.log(yixian);
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

  .div01 {
    color: #0e0e0e;
    font-size: 25px;
    margin-top: 30px;
    margin-left: 10px;
  }

  .div01 img {
    margin-right: 20px;
  }

  .a01 div:after {
    content: " ";
    display: inline-block;
    width: 100%;
  }

  .d {
    color: #BDBDBD;
  }

  .c {
    color: #0e0e0e;
  }

  select::-ms-expand {
    display: none;
  }

  select {
    cursor: pointer;
    appearance: none;
    -moz-appearance: none;
    -webkit-appearance: none;
    font-size: 15px;
    border: solid rgba(153, 153, 153, 0.65) 1px;
  }

  .we {
    margin-left: 50px;
    margin-top: 30px;
  }

  form {

    margin-top: 20px;
    color: #BDBDBD;
  }

  .hukou {
    display: flex;
    line-height: 2.5em;
    margin-top: 20px;
    padding-left: 5px;
  }

  div span {
    color: #BDBDBD;
  }

  .btn {
    position: relative;
    width: 80px;
    height: 50px;
    background: rgba(180, 3, 3, 0.8);
    color: white;
    margin-top: 50px;
    margin-left: 400px;
  }
</style>
