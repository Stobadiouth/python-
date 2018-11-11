<template>
  <div>
    <ul class="row">
      <li class="er01-css">
        <input id="selectTravelCity" type="text" :value="b" readonly="readonly" >
        <ul class="my01-css my01"  >
          <li v-for="lu in language">
          <input name="box"  @click="re($event)" :value="lu.name" type="checkbox" :id="'checkbox'+lu.id" class="regular-checkbox"/><label
          class="k01" :for="'checkbox'+lu.id"></label><span v-text="lu.name"></span>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>


<script>
  export default {
    name: 'Languagechange',
    data() {
      return {
        language: [{id:1,name:'普通话'},
          {id:2,name:'广东话'},
          {id:3,name:'英语'},
          {id:4,name:'法语'},
          {id:5,name:'日语'},
          {id:6,name:'韩语'},
          {id:7,name:'德语'},
          {id:8,name:'意大利语'},
          {id:9,name:'俄语'},
          {id:10,name:'芬兰语'},
          {id:11,name:'荷兰语'},
          {id:12,name:'葡萄牙语'},
          {id:13,name:'西班牙语'},
          {id:14,name:'越南语'},
          {id:15,name:'阿拉伯语'},
          {id:16,name:'泰语'},
          {id:17,name:'印度语'},
          {id:18,name:'丹麦语'},
          {id:19,name:'希腊语'},
          {id:20,name:'伊朗语'},
          {id:21,name:'匈牙利语'},
          {id:22,name:'土耳其语'},
          {id:23,name:'挪威语'},
          {id:24,name:'捷克语'},
          {id:25,name:'波兰语'},
          {id:26,name:'瑞典语'},
          {id:27,name:'缅甸语'},
          {id:28,name:'其他'},
          ],
        b: [],
        flag: 'false'
      }
    },
    methods: {
      re:function (e) {
        let checked=e.target.checked;
        let a=e.target.value;
        if(checked){
          this.b.push(a);
        }else{
          this.b.pop(a);
        }

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

  .er01-css .my01-css {
    position: absolute;
    z-index: 3;
    width: 300px;
    background: white;
    border: solid rgba(153, 153, 153, 0.65) 1px;
    display: none;
  }

  .er01-css:hover .my01-css {
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
    padding-left: 10px;
    color: black;
    width: 90px;
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
    top: -9px;
    left:0px;
    color: #F23A6E;
  }

  input#selectTravelCity {
    width: 15.5em;
    height: 2.5em;
    padding: 0.2em 0.4em 0.2em 0.4em;
    vertical-align: middle;
    border: 1px solid #e9e9e9;
    -moz-border-radius: 0.2em;
    -webkit-border-radius: 0.2em;
    border-radius: 0.2em;
    box-shadow: inset 0 0 3px #a0a0a0;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    /* sample image from the webinfocentral.com */
    background: url(http://webinfocentral.com/Images/favicon.ico) 95% / 10% no-repeat #fdfdfd;
    font-family: Arial, Calibri, Tahoma, Verdana;
    font-size: 1.1em;
    color: #0e0e0e;
    cursor: pointer;
  }
  input#selectTravelCity:hover{
    color: #F23A6E;
  }

</style>
