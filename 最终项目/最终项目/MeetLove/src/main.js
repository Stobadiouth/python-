// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import NavHeader from './components/NavHeader'
import NavBottom from './components/NavBottom'
import Identify from './components/Identify'
import ShenShi from './components/Shengshi'
import Material from './components/Material'
import Photo from './components/Photo'
import Name from './components/Name'
import Phone from './components/Phone'
import Friend from './components/Friend'
import Root from './components/Root'
import Myactive from './components/Myactive'
import Ziliaojindu from './components/Ziliaojindu'
import Perziliao from './components/Perziliao'
import Shengshiqu from './components/Shengshiqu'
import Gerenxuanyan from './components/Gerenxuanyan'
import Personaldetails from './components/Personaldetails'
import Wangsong from './components/Wangsong'
import Xialakuang from './components/Xialakuang'
import Languagechange from './components/Languagechange'
import Hobby from './components/Hobby'
import Member from './components/Member'
import Yixiang from './components/Yixiang'
import Seeme from './components/Seeme'
import Jinbi from './components/Jinbi'
import Jifen from './components/Jifen'
import Xuexiao from './components/Xuexiao'
import VIP from './components/VIP'
import axios from 'axios'
import Qs from 'qs'
//QS是axios库中带的，不需要我们再npm安装一个

Vue.prototype.axios = axios;
Vue.prototype.qs = Qs;

Vue.config.productionTip = false

//注册全局组件
Vue.component('nav-head',NavHeader);
Vue.component('nav-bottom',NavBottom);
Vue.component('identify',Identify);
Vue.component('sele-ss',ShenShi);

Vue.component('material',Material);
Vue.component('photo',Photo);
Vue.component('name',Name);
Vue.component('phone',Phone);
Vue.component('friend',Friend);
Vue.component('root',Root);
Vue.component('myactive',Myactive);
Vue.component('ziliaojindu',Ziliaojindu);
Vue.component('perziliao',Perziliao);
Vue.component('shengshiqu',Shengshiqu);
Vue.component('gerenxuanyan',Gerenxuanyan);
Vue.component('personaldetails',Personaldetails);
Vue.component('wangsong',Wangsong);
Vue.component('xialakuang',Xialakuang);
Vue.component('languagechange',Languagechange);
Vue.component('hobby',Hobby);
Vue.component('member',Member);
Vue.component('yixiang',Yixiang);
Vue.component('seeme',Seeme);
Vue.component('jinbi',Jinbi);
Vue.component('jifen',Jifen);
Vue.component('xuexiao',Xuexiao);
Vue.component('vip',VIP);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
