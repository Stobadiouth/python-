<template>
  <div class="row">
    <select id="selectTravelCity" v-model="m"  @change="me($event)" :title="key01">
      <option v-for="i of message"  v-text="i"></option>
    </select>
  </div>

</template>

<script>
export default {
  name: 'Xialakuang',
  props:{
    message:'',
    key01:'',
    valu:''

  },
  data () {
    return {
      m: '',
    }
  },
  mounted(){
    this.panduan()
    //如果没有这句代码，select中初始化会是空白的，默认选中就无法实现

  },
  methods:{
    panduan:function(){
      if (this.valu[this.key01])   {
        if (this.key01=='你的体重'){
          let i=this.valu[this.key01]+'公斤';
          this.m = i
        }else {
          let i=this.valu[this.key01];
          this.m = i
        }
      }else{
        this.m=this.message[0]
      }
    },
    me:function (event) {
      let a=event.target.title;
      let mes01=[a,this.m];
      this.$emit("mes",mes01)
    }
  },
  watch:{
    valu:function(){
      this.panduan()
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  select#selectTravelCity
  {
    width                    : 15.5em;
    height                   : 2.5em;
    padding                  : 0.2em 0.4em 0.2em 0.4em;
    vertical-align           : middle;
    border                   : 1px solid #e9e9e9;
    -moz-border-radius       : 0.2em;
    -webkit-border-radius    : 0.2em;
    border-radius            : 0.2em;
    box-shadow               : inset 0 0 3px #a0a0a0;
    -webkit-appearance       : none;
    -moz-appearance          : none;
    appearance               : none;
    /* sample image from the webinfocentral.com */
    /*background               : url(http://webinfocentral.com/Images/favicon.ico) 95% / 10% no-repeat #fdfdfd;*/
    font-family              : Arial,  Calibri, Tahoma, Verdana;
    font-size                : 1.1em;
    color                    : #0e0e0e;
    cursor                   : pointer;
  }
  select#selectTravelCity  option
  {
    font-size               : 1em;
    padding                 : 0.2em 0.4em 0.2em 0.4em;
  }
  select#selectTravelCity  option[selected]{ font-weight:bold}
  select#selectTravelCity  option:nth-child(even) { background-color:#f5f5f5; }
  select#selectTravelCity:hover
  {
    color                   : #F23A6E;
    border                  : 1px solid #cdcdcd;
  }
  select#selectTravelCity:focus {box-shadow: 0 0 2px 1px #F23A6E;}

</style>
