<template>
  <div>
    <div class="row dd" @click="changecolor" :class="{ll:q==1}"><span >喜爱的电影</span></div>
    <ul class="row">
      <li class="er01-css">
        <ul class="my01-css my01 or"  :class="{ol:q==1}">
          <li v-for="lu in language">
            <input name="box"  @click="mov($event)" :value="lu.name" type="checkbox"  :id="'checkbox'+lu.id" class="regular-checkbox"/><label
            class="k01" :for="'checkbox'+lu.id"></label><span v-text="lu.name"></span>
          </li>
        </ul>
      </li>
    </ul>
    <div class="row dd" @click="changecolor01" :class="{ll:n==1}"><span >喜爱的音乐</span></div>
    <ul class="row">
      <li class="er01-css">
        <ul class="my01-css my01 or"  :class="{ol:n==1}">
          <li v-for="lu in music">
            <input name="box"  @click="mus($event)" :value="lu.name" type="checkbox" :id="'music'+lu.id" class="regular-checkbox"/><label
            class="k01" :for="'music'+lu.id"></label><span v-text="lu.name"></span>
          </li>
        </ul>
      </li>
    </ul>
    <div class="row dd" @click="changecolor02" :class="{ll:m==1}"><span >喜爱的书籍</span></div>
    <ul class="row">
      <li class="er01-css">
        <ul class="my01-css my01 or"  :class="{ol:m==1}">
          <li v-for="lu in book">
            <input name="box"  @click="boo($event)" :value="lu.name" type="checkbox" :id="'book'+lu.id" class="regular-checkbox"/><label
            class="k01" :for="'book'+lu.id"></label><span v-text="lu.name"></span>
          </li>
        </ul>
      </li>
    </ul>
    <div class="row dd" @click="changecolor03" :class="{ll:p==1}"><span >喜爱的宠物</span></div>
    <ul class="row">
      <li class="er01-css">
        <ul class="my01-css my01 or"  :class="{ol:p==1}">
          <li v-for="lu in pet">
            <input name="box"  @click="pe($event)" :value="lu.name" type="checkbox" :id="'pet'+lu.id" class="regular-checkbox"/><label
            class="k01" :for="'pet'+lu.id"></label><span v-text="lu.name"></span>
          </li>
        </ul>
      </li>
    </ul>
    <div class="row dd" @click="changecolor04" :class="{ll:w==1}"><span >喜爱的食物</span></div>
    <ul class="row">
      <li class="er01-css">
        <ul class="my01-css my01 or"  :class="{ol:w==1}">
          <li v-for="lu in food">
            <input name="box"  @click="foo($event)" :value="lu.name" type="checkbox" :id="'food'+lu.id" class="regular-checkbox"/><label
            class="k01" :for="'food'+lu.id"></label><span v-text="lu.name"></span>
          </li>
        </ul>
      </li>
    </ul>
    <div v-text="tishi04" style="color: red;font-size: 20px;font-weight: bolder;margin-left: 380px;padding-top:100px"></div>
    <button class="btn" @click="savelike($event)">保存</button>
  </div>
</template>


<script>
  import axios from 'axios';
  import $ from 'jquery';

  export default {
    name: 'Hobby',
    data() {
      return {
        tishi04:'',
        movename:'',
        q:0,
        n:0,
        m:0,
        p:0,
        w:0,
        language: [
          {id:2,name:'故事片'},
          {id:3,name:'文艺爱情'},
          {id:4,name:'科幻'},
          {id:5,name:'动作武侠'},
          {id:6,name:'侦探推理'},
          {id:7,name:'实验电影'},
          {id:8,name:'老电影'},
          {id:9,name:'限制级电影'},
          {id:10,name:'儿童/卡通片'},
          {id:11,name:'纪录片'},
          {id:12,name:'西部电影'},
          {id:13,name:'恐怖'},
          {id:14,name:'得奖电影'},
          {id:15,name:'艺术电影'},
          {id:16,name:'音乐歌舞'},
          {id:17,name:'肥皂剧'},
          {id:18,name:'喜剧'},
          {id:19,name:'其他'},
          {id:20,name:'什么都看'},

        ],
        music: [{id:1,name:'中文流行音乐'},
          {id:2,name:'轻音乐'},
          {id:3,name:'民族音乐'},
          {id:4,name:'老歌'},
          {id:5,name:'舞曲'},
          {id:6,name:'歌剧'},
          {id:7,name:'西部乡村'},
          {id:8,name:'英文流行音乐'},
          {id:9,name:'交响乐'},
          {id:10,name:'地方戏曲'},
          {id:11,name:'摇滚'},
          {id:12,name:'另类'},
          {id:13,name:'灵歌'},
          {id:14,name:'爵士/蓝调'},
          {id:15,name:'其他'},

        ],
        book: [{id:1,name:'校园青春'},
          {id:2,name:'文学'},
          {id:3,name:'艺术与摄影'},
          {id:4,name:'励志与成功'},
          {id:5,name:'动漫与幽默'},
          {id:6,name:'政治与军事'},
          {id:7,name:'哲学与宗教'},
          {id:8,name:'历史传记'},
          {id:9,name:'运动健身'},
          {id:10,name:'健康与养生'},
          {id:11,name:'烹饪与饮食'},
          {id:12,name:'投资理财'},
          {id:13,name:'旅游'},
          {id:14,name:'婚恋与家庭'},
          {id:15,name:'期刊杂志'},
          {id:16,name:'娱乐时尚'},
          {id:17,name:'人文社科'},
          {id:18,name:'自然科学'},
          {id:19,name:'收藏与鉴赏'},
          {id:20,name:'其他'},
          {id:21,name:'什么都看'},
        ],
        pet: [{id:1,name:'狗'},
          {id:2,name:'猫'},
          {id:3,name:'鱼'},
          {id:4,name:'兔'},
          {id:5,name:'鸟'},
          {id:6,name:'乌龟'},
          {id:7,name:'蜥蜴'},
          {id:8,name:'鼠'},
          {id:9,name:'蛇'},
          {id:10,name:'另类宠物'},
        ],
        food: [{id:1,name:'川菜'},
          {id:2,name:'江浙菜'},
          {id:3,name:'湘菜'},
          {id:4,name:'火锅'},
          {id:5,name:'烧烤'},
          {id:6,name:'家常菜'},
          {id:7,name:'路边摊'},
          {id:8,name:'健康食品'},
          {id:9,name:'零食'},
          {id:10,name:'粤菜'},
          {id:11,name:'北方菜'},
          {id:12,name:'面食'},
          {id:13,name:'素食'},
          {id:14,name:'甜食'},
          {id:15,name:'自助餐'},
          {id:16,name:'减肥餐'},
          {id:17,name:'吃饱就好'},
          {id:18,name:'其他'},
        ],
        likemove: [],
        likemusic: [],
        likebook: [],
        likepet: [],
        likefood: [],

      }
    },
    mounted: function () {
      this.gethobby();

    },
    methods: {
      gethobby:function(){
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/gethobby/',params)
          .then(function (response) {
            // console.log(response.data["food"]);
            let food=response.data["food"].split(',');
            let pet=response.data["pet"].split(',');
            let book=response.data["book"].split(',');
            let music=response.data["music"].split(',');
            let film=response.data["film"].split(',');
              vm.likemove=film;
              vm.likemusic=pet;
              vm.likebook=book;
              vm.likepet=music;
              vm.likefood=food;


          });
      },
      mov:function (e) {
        let checked=e.target.checked;
        let a=e.target.value;
        if(checked){
          this.likemove.push(a);
        }else{
          let index = this.likemove.indexOf(a);
          this.likemove.splice(index, 1);

        }
        console.log(this.likemove);
      },
      mus:function (e) {
        let checked=e.target.checked;
        let a=e.target.value;
        if(checked){
          this.likemusic.push(a);
        }else{
          let index = this.likemusic.indexOf(a);
          this.likemusic.splice(index, 1);
        }
      },
      boo:function (e) {
        let checked=e.target.checked;
        let a=e.target.value;
        if(checked){
          this.likebook.push(a);
        }else{
          let index = this.likebook.indexOf(a);
          this.likebook.splice(index, 1);
        }
        console.log(this.likebook);
      },
      pe:function (e) {
        let checked=e.target.checked;
        let a=e.target.value;
        if(checked){
          this.likepet.push(a);
        }else{
          let index = this.likepet.indexOf(a);
          this.likepet.splice(index, 1);
        }
      },
      foo:function (e) {
        let checked=e.target.checked;
        let a=e.target.value;
        if(checked){
          this.likefood.push(a);
        }else{
          let index = this.likefood.indexOf(a);
          this.likefood.splice(index, 1);
        }
        console.log(this.likefood);
      },
      changecolor:function () {
        let a=document.getElementsByTagName("input");
        for (let i of a){
          for( let o of this.likemove){
            if (i.value==o) {
              i.checked=true
            }
          }
        }
        if (this.q==0){
          this.q=1
        } else {
          this.q=0
        }
      },
      changecolor01:function () {
        let a=document.getElementsByTagName("input");
        for (let i of a){
          for( let o of this.likemusic){
            if (i.value==o) {
              i.checked=true
            }
          }
        }
        if (this.n==0){
          this.n=1
        } else {
          this.n=0
        }
      },
      changecolor02:function () {
        let a=document.getElementsByTagName("input");
        for (let i of a){
          for( let o of this.likebook){
            if (i.value==o) {
              i.checked=true
            }
          }
        }
        if (this.m==0){
          this.m=1
        } else {
          this.m=0
        }
      },
      changecolor03:function () {
        let a=document.getElementsByTagName("input");
        for (let i of a){
          for( let o of this.likepet){
            if (i.value==o) {
              i.checked=true
            }
          }
        }
        if (this.p==0){
          this.p=1
        } else {
          this.p=0
        }
      },
      changecolor04:function () {
        let a=document.getElementsByTagName("input");
        for (let i of a){
          for( let o of this.likefood){
            if (i.value==o) {
              i.checked=true
            }
          }
        }
        if (this.w==0){
          this.w=1
        } else {
          this.w=0
        }
      },
      savelike:function () {
        let id=localStorage.getItem('id');
        let like={
          id:id,
          likemove: this.likemove,
          likemusic: this.likemusic,
          likebook: this.likebook,
          likepet: this.likepet,
          likefood: this.likefood,
        };
        let vm=this;
        $.ajax(
          {
            url:'http://47.106.14.132:8000/user/likehobby/',
            type:"POST",
            data:JSON.stringify(like),
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
      }






    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul, li, span, label {
    margin: 0;
    padding: 0;
    list-style: none;
  }
  .dd{
    line-height:30px;
    margin-top: 20px;
    font-family: "微软雅黑", "黑体";
    font-weight: bolder;
  }
  .dd:hover{
    color: #F23A6E;
    cursor: pointer;
  }
  .ll{
    color: #FFFFFF;
    width: 100%;
    height: 30px;
    background: rgba(242, 58, 110, 0.53);
  }

  .er01-css .my01-css {
    /*position: absolute;*/
    /*z-index: 3;*/
    width:100%;
    margin-left:-15px;
    background: white;
    /*border: solid rgba(153, 153, 153, 0.65) 1px;*/

  }
  .or{
    display: none;
  }

  .ol{
    display: block;
  }

  .er01-css .my01-css :hover {
    cursor: pointer;
  }

  /*开始复选框*/
  .er01-css .my01 span {
    display: inline-block;
    margin-left: 5px;
  }

  .regular-checkbox {
    display: none;
  }

  .er01-css .my01 li {
    display: inline-block;
    padding-top: 20px;
    padding-left: 10px;
    color: black;
    width:120px;
    height: 30px;
  }

  .regular-checkbox + label {
    background-color: #fafafa;
    border: 1px solid #cacece;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05), inset 0px -15px 10px -12px rgba(0, 0, 0, 0.05);
    padding: 6px;
    border-radius: 3px;
    display: inline-block;
    position: relative;
  }

  .regular-checkbox + label:active, .regular-checkbox:checked + label:active {
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05), inset 0px 1px 3px rgba(0, 0, 0, 0.1);
  }

  .regular-checkbox:checked + label {
    background-color: #e9ecee;
    border: 1px solid #adb8c0;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05), inset 0px -15px 10px -12px rgba(0, 0, 0, 0.05), inset 15px 10px -12px rgba(255, 255, 255, 0.1);
    color: #99a1a7;
  }

  .regular-checkbox:checked + label:after {
    content: '\2714';
    font-size: 14px;
    position: absolute;
    top: -3px;
    left:0px;
    color: #F23A6E;
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
