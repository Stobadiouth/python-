<template>
  <div>
    <div class="row b">
      基本信息 <span>为了保证资料真实有效，灰色字体信息不得随意修改。</span>
    </div>
    <form name="date" class="form-inline">
      <div class="col-md-9 col-sm-6 right" style="display: block">
        <div class="div-lable">昵称：
          <input type="text" v-model="name" class="form-control">
        </div>
        <div class="div-lable">性别：
          <input value="1" type="radio" v-model="nn" name="1"/>男
          <input value="0" type="radio" v-model="nn" name="0"/>女
        </div>
        <div class="div-lable">生日：
          <form name="date">
            <select name="year" class="form-control" v-model="changeyear">
              <option v-for="i in year" v-text="i"></option>
            </select><span>年</span>
            <select name="month" class="form-control" v-model="changemonth" @change="update">
              <option v-for="i in month" v-text="i"></option>
            </select><span>月</span>
            <select name="day" class="form-control" v-model="changdate">
              <option v-for="i in date" v-text="i"></option>
            </select><span>日</span>
          </form>
        </div>
        <div class="div-lable">身高：
          <form>
            <select name="height" class="form-control" v-model="changeheight">
              <option v-for="i in height" v-text="i"></option>
            </select><span>cm</span>
          </form>

        </div>
        <div class="div-lable">婚姻状况：
          <select class="form-control" v-model="marry">
            <option >未婚</option>
            <option >离异</option>
            <option>丧偶</option>
          </select>
        </div>
        <div class="div-lable">工作地：
          <div class="form-control" style="line-height:30px;width: 110px;text-align: center;overflow: hidden" v-text="dd"></div>
        </div>
        <div class="div-lable form-group">更改工作地：
          <shengshiqu @d01="d02"></shengshiqu>
        </div>
        <div class="div-lable ">学历：

          <select class="form-control" v-model="study">
            <option>选择学历</option>
            <option>高中及以下</option>
            <option>中专</option>
            <option>大专</option>
            <option>大学本科</option>
            <option>硕士</option>
            <option>博士</option>
          </select>
        </div>
        <div class=" div-lable">年收入：
          <select class="form-control" v-model="income">
            <option>你的年收入</option>
            <option>1-5万元</option>
            <option>5-10万元</option>
            <option>10-15万元</option>
            <option>15-20万元</option>
            <option>20-35万元</option>
            <option>35万元以上</option>
          </select>
        </div>
        <div v-text="tishi04" style="color: red;font-size: 20px;font-weight: bolder;margin-left: 380px;padding-top:100px"></div>
        <button class="btn" @click.stop.prevent="baocun">保存</button>
      </div>
    </form>
  </div>

</template>
<script>
  import axios from 'axios';

  export default {
    name: 'Perziliao',
    data() {
      return {
        tishi04:'',
        dd:"北京北京东城区",
        name: '凉笙',
        nn: '0',
        a: '',
        changeyear: '1994',
        changemonth: '01',
        changdate: '02',
        changeheight: 177,
        marry:'离异',
        study:'大学本科',
        income:'你的年收入',
        year: [],
        month: [],
        date: [],
        height: []
      }
    },
    mounted: function () {
      // 在开始页面时生成日期---------
      this.upyear();
      this.upmonth();
      this.upheight();
      this.quname();
    },
    methods: {
      changename:function(){
        this.$emit('namechange',this.name)
      },
      baocun:function(){
        let id = localStorage.getItem('id');
        let params = new URLSearchParams();
        params.append("id", id);
        params.append("name", this.name);
        params.append("sex", this.nn);
        params.append("birth", this.changeyear+'-'+this.changemonth+'-'+this.changdate);
        params.append("height", this.changeheight);
        params.append("marry", this.marry);
        params.append("city", this.dd);
        params.append("edu__edu", this.study);
        params.append("income", this.income);
        axios.post('http://47.106.14.132:8000/user/changenessage/', params)
        this.changename()
      },
      d02:function(q){
        this.dd=q[0]
      },
      quname: function () {
        let vm = this;
        let id = localStorage.getItem('id');
        let params = new URLSearchParams();
        params.append('id', id);
        axios.post('http://47.106.14.132:8000/user/quname/', params)
          .then(function (response) {
            vm.name = response.data.name;
            vm.nn = response.data.sex;
            let a = response.data.birth;
            vm.changeyear = a.split("-")[0];
            vm.changemonth=a.split("-")[1];
            vm.changdate=a.split("-")[2];
            vm.changeheight=response.data.height;
            vm.marry=response.data.marry;
            vm.dd=response.data.city;
            vm.study=response.data.edu__edu;
            vm.income=response.data.income__income;
          })
      },
      upyear: function () {
        let vm = this;
        for (let i = 1950; i < 2018; i++) {
          vm.year.push(i)
        }
      },
      upmonth: function () {
        let vm = this;
        for (let i = 1; i < 13; i++) {
          if(i<10){
            i='0'+i
          }
          vm.month.push(i)
        }
        this.update()
      },
      update: function () {
        this.date = [];
        let m=['01','03','05','07','08','10','12'];
        let n=['04','06','09','11'];
        let mm=m.indexOf(this.changemonth);
        let nn=n.indexOf(this.changemonth);
        if(mm!=-1){
          for (let i = 1; i < 32; i++) {
                if(i<10){
                  i='0'+i
                }
                this.date.push(i)
              }
        }else if(nn!=-1){
          for (let i = 1; i < 31; i++) {
            if(i<10){
              i='0'+i
            }
            this.date.push(i)
          }
        }else if(this.changemonth == 2 && this.IsPinYear()){
          for (let i = 1; i < 30; i++) {
            if(i<10){
              i='0'+i
            }
                this.date.push(i)
              }
        }else {
          for (let i = 1; i < 29; i++) {
            if(i<10){
              i='0'+i
            }
                  this.date.push(i)
        }
        }
      },
      IsPinYear: function () {
        let year = this.changeyear;
        return (0 == year % 4 && (year % 100 != 0 || year % 400 == 0));
      },
      // 生成日期结束----------------------
      upheight: function () {
        for (let i = 140; i < 210; i++) {
          this.height.push(i)
        }
      },


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

  select::-ms-expand {
    display: none;
  }

  select {
    appearance: none;
    -moz-appearance: none;
    -webkit-appearance: none;
    font-size: 15px;
    border: solid rgba(153, 153, 153, 0.65) 1px;
  }

  a {
    color: white;
    text-decoration: none;
  }

  a:hover {
    text-decoration: solid underline white;
  }

  li {
    list-style: none;
    background: rgba(255, 0, 0, 0);
    float: left;
  }

  .b {
    color: rgba(0, 0, 0, 0.66);
    font-size: 18px;
    margin-left: 10px;
    margin-top: 10px;
  }

  .b span {
    color: #BDBDBD;
    font-size: 14px;
  }

  .div-lable {
    margin-top: 20px;
  }

  .div-lable [type='text'] {
    width: 120px;
  }

  .right {
    padding-top: 30px;
    padding-left: 100px;
    display: none;
  }

  .div-lable [type='radio'] {
    margin-left: 20px;
  }

  .div-lable form, input {
    display: inline;
  }

  .btn {
    width: 80px;
    height: 50px;
    background: rgba(180, 3, 3, 0.8);
    color: white;
    margin-left: 400px;
    margin-top: 100px;
  }


</style>
