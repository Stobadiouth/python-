import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/Index'
import Home from '@/components/Home'
import Active from '@/components/Active'
import ActiveMess from '@/components/ActiveMess'
import Luntan from '@/components/Luntan'
import Personal from '@/components/Personal'
import Search from '@/components/Search'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Member from '@/components/Member'
import Ltxq from '@/components/Ltxq'
import About from '@/components/About'
import Email from '@/components/Email'
import Buy from '@/components/Buy'
import Shimingrenzheng from '@/components/Shimingrenzheng'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index,
      children:[
        {
          path:'',
          name:'home',
          component:Home
        },
        {
          path:'active',
          name:'active',
          component:Active
        },
        {
          path:'activemess',
          name:'activemess',
          component:ActiveMess
        },
        {
          path:'luntan',
          name:'luntan',
          component:Luntan
        },
        {
          path: 'ltxq/:invid',
          name: 'Ltxq',
          component: Ltxq,
        },
        {
          path:'personal',
          name:'personal',
          component:Personal
        },
        {
          path:'search',
          name:'search',
          component:Search
        },
        {
          path:'member/:userid',
          name:'member',
          component:Member
        },
        {
          path:'email',
          name:'email',
          component:Email
        },
        {
          path: 'buy',
          name: 'Buy',
          component: Buy,
        },{
          path: 'shimingrenzheng',
          name: 'Shimingrenzheng',
          component: Shimingrenzheng,
        },
      ]
    },
    {
      path:'/login',
      name:'login',
      component:Login
    },
    {
      path:'/register',
      name:'register',
      component:Register
    },
    {
      path:'/about',
      name:'about',
      component:About
    },

  ]
})
