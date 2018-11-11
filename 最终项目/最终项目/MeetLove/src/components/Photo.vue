<template>
  <div>
    <div class="row">
      <div class="col-md-3 div-lable">
        我的头像：
        <img :src="picture" class="img-thumbnail" style="margin-top: 20px">
      </div>
      <div class="col-md-9">
        <button type="button" class="btn btn-warning ">设置头像
          <input type="file" class="bt" @change="touxian"></button>

        <div><span>{{massage}}</span></div>
      </div>
    </div>
    <div style="margin-top: 20px;font-size: 19px">我的相册：</div>
    <div class="row">
      <div class="col-md-3 div-lable">
        <img :src='photo' class="img-thumbnail">
      </div>
      <!--<div class="col-md-3 div-lable ji" :class="{ji01:a==1}">-->
        <!--<img id="ji01" class="img-thumbnail ">-->
      <!--</div>-->
      <div class="col-md-3">
        <input type="file" name="addimg" id="addimg" @change="changeimg($event)" @mouseover="imgchange02"
               @mouseout="imgchange01">
        <img :src=src01 class="imgadd">
      </div>
    </div>
  </div>


</template>
<script>
  import axios from 'axios';
  import 上传 from "../assets/personal/上传.png"
  import 上传颜色 from "../assets/personal/上传颜色.png"

  export default {
    name: 'Perziliao',
    data() {
      return {
        photo:'',
        picture: '',
        massage: "",
        src01: 上传,
        url: '',
        a: 0
      }
    },
    mounted: function () {
      this.touxiang();

    },
    methods: {
      touxiang: function () {
        let params = new URLSearchParams();
        let id=localStorage.getItem('id');
        params.append('id', id);
        let vm=this;
        axios.post('http://47.106.14.132:8000/user/xianshitouxiang/',params)
          .then(function (response) {
            let s=response.data.touxiang;
            let s01=response.data.zhaopian;
            vm.photo='http://ph6s7as96.bkt.clouddn.com/'+s;
            vm.picture=s01;
            if (vm.picture) {
              vm.massage = "恭喜您已成为有照片用户，更多的会员会选择有照片的用户进行联系，快去完善更多详细资料吧！"
            } else {
              vm.massage = "好看的人早已上传了头像，要不要来试一试！"
            }
          });




      },
      touxian: function (e) {
          let vm=this;
          let file = e.target.files[0];
          this.preview01(file);
          // 和后端请求文件名称
          axios.get('http://47.106.14.132:8000/user/qiniutoken/?key=' + file.name)
            .then(function (response) {
              console.log(response);
              let token = response.data.token;
              let newname = response.data.key;
              let qiniu = require('qiniu-js');
              // 给文件重新命名
              let newfile = new File([file], newname);
              // 更改配置文件准备传给七牛云
              let config = {
                useCdnDomain: false,
                disableStatisticsReport: true,
                retryCount: 6,
                region: qiniu.region.z0
              };
              let putExtra = {
                fname: "",
                params: {},
                mimeType: ["image/png", "image/jpeg", "image/gif"]
              };
              let key = newfile.name;
              // 添加上传dom面板
              putExtra.params["x:name"] = key.split(".")[0];

              // 调用sdk上传接口获得相应的observable，控制上传和暂停
              let observable = qiniu.upload(file, key, token, putExtra);

              let subscription = observable.subscribe({
                next(res) {

                },
                error(err) {
                  alert('error！')
                },
                complete(res) {
                  let id=localStorage.getItem('id');
                  let src=res.key;
                  let params = new URLSearchParams();
                  params.append('id', id);
                  params.append('src',src);
                  axios.post('http://47.106.14.132:8000/user/img/',params)
                    .then(function (response) {
                        vm.$emit('pic',vm.picture)
                    })
                }
              });

            })
            .catch(function (error) {
              console.log(error);
            })

        },

      preview01: function (file) {
        this.picture = URL.createObjectURL(file);


      },
      imgchange02: function () {
        this.src01 = 上传颜色
      },
      imgchange01: function () {
        this.src01 = 上传
      },
      changeimg: function (e) {
        let file = e.target.files[0];
        this.photo = URL.createObjectURL(file);
        // 和后端请求文件名称
        axios.get('http://47.106.14.132:8000/user/qiniutoken/?key=' + file.name)
          .then(function (response) {
            console.log(response);
            let token = response.data.token;
            let newname = response.data.key;
            let qiniu = require('qiniu-js');
            // 给文件重新命名
            let newfile = new File([file], newname);
            // 更改配置文件准备传给七牛云
            let config = {
              useCdnDomain: false,
              disableStatisticsReport: true,
              retryCount: 6,
              region: qiniu.region.z0
            };
            let putExtra = {
              fname: "",
              params: {},
              mimeType: ["image/png", "image/jpeg", "image/gif"]
            };
            let key = newfile.name;
            // 添加上传dom面板
            putExtra.params["x:name"] = key.split(".")[0];

            // 调用sdk上传接口获得相应的observable，控制上传和暂停
            let observable = qiniu.upload(file, key, token, putExtra);

            let subscription = observable.subscribe({
              next(res) {
                // ...
              },
              error(err) {
                alert('error！')
              },
              complete(res) {

                let id=localStorage.getItem('id');
                let src=res.key;
                let params = new URLSearchParams();
                params.append('id', id);
                params.append('src',src);
                axios.post('http://47.106.14.132:8000/user/uptouxiang/',params)
                  .then(function (response) {

                  })
              }
            });

          })
          .catch(function (error) {
            console.log(error);
          })

      },
      // preview1: function (file) {
      //   this.url = URL.createObjectURL(file);
      //   document.getElementById("ji01").src = this.url;
      //   this.a = 1
      //
      // }


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

  .div-lable {
    margin-top: 20px;
    color: #0e0e0e;
    font-size: 19px;
  }

  .div-lable img {
    margin-left: 20px;
    width: 185px;
    height: 185px;
  }

  .btn {
    margin-top: 80px;
    margin-left: 50px;
    width: 100px;
    background: #FF7F00;

  }

  .bt {
    width: 100px;
    position: relative;
    margin-top: -25px;
    /*padding-top: 10px;*/
    margin-left: -10px;
    right: 0;
    top: 0;
    opacity: 0;

  }

  .btn:hover {
    background: #F36500;
  }

  span {
    margin-top: 20px;
    display: block;
    text-align: left;
    margin-left: 60px;
    color: #A5ADC5;
  }

  .col-md-9 img {
    width: 185px;
    height: 185px;
    margin-left: 20px;
    margin-top: 45px;
  }

  #addimg {
    margin-top: 30px;
    width: 170px;
    height: 170px;
    position: relative;
    z-index: 2;
    opacity: 0;
    cursor: pointer;
  }

  .imgadd {
    position: relative;
    top: -185px;
    left: -18px;
  }

  .ji {
    display: none;
  }

  .ji01 {
    display: block;
  }


</style>
