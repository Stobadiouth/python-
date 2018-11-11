<template>
    <ul class="row">
      <li class="er01-css">
        <input id="selectTravelCity" type="text" :value="b" readonly="readonly" >
        <ul class="my01-css my01">
          <li v-for="lu in language">
          <input name="box"  @click="re($event)"  :value="lu.name" type="checkbox" :id="'checkbox'+lu.id" class="regular-checkbox"/><label
          class="k01" :for="'checkbox'+lu.id"></label><span v-text="lu.name"></span>
          </li>
        </ul>
      </li>
    </ul>

</template>


<script>
  export default {
    name: 'Yixiang',
    props:{
      language:''
    },
    data() {
      return {
        b:[],
        flag: 'false'
      }
    },
    watch:{
      b:function () {
        this.$emit('ch01',this.b)
      }
    },
    methods: {
      re:function (e) {
        let checked=e.target.checked;
        let a=e.target.value;
        let ck=e.target.id;
        if(checked){
          if(a=='不限'){
            let box=document.getElementsByName('box');
            if( ck=='checkbox1'){
              for(let j=1;j<4;j++){
                box[j].checked=false;
                box[j].disabled=true;
              }
              this.b=[];
              this.b.push(a);
            }else{
              for(let j=13;j<17;j++){
                box[j].checked=false;
                box[j].disabled=true;
              }
              this.b=[];
              this.b.push(a);
            }

          }else{
            this.b.push(a);
          }

        }else{
          let box=document.getElementsByName('box');
          if( ck=='checkbox1'){
            for(let j=1;j<4;j++){
              box[j].disabled=false;
            }
            this.b.pop(a);
          }else if (ck=='checkbox13') {
            for(let j=13;j<17;j++){
              box[j].disabled=false;
            }
            this.b.pop(a);
          }else{
            this.b.pop(a);
          }
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
    background: white;
    z-index: 3;
    width:255px;
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
    width:200px;
    height: 30px;
  }

  .regular-checkbox + label {
    border: 1px solid #cacece;
    padding: 6px;
    border-radius: 3px;
    display: inline-block;
    position: relative;
  }



  .regular-checkbox:checked + label {
    background-color: #e9ecee;
    border: 1px solid #adb8c0;
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
    width: 16.5em;
    height: 2.5em;
    padding: 0.2em 0.4em 0.2em 0.4em;
    vertical-align: middle;
    border: solid rgba(153, 153, 153, 0.65) 1px;
    -moz-border-radius: 0.2em;
    -webkit-border-radius: 0.2em;
    border-radius: 0.2em;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    font-family: Arial, Calibri, Tahoma, Verdana;
    font-size: 1.1em;
    color: #0e0e0e;
    cursor: pointer;
  }
</style>
