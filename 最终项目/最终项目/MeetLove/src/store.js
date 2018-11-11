
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
  /*
  * state指的就是储存的数据，
  * 下面的数据是我在项目中需要用的数据字段
  * */
  state:{
    index:1,
    user_id:'',
  },
  /*
    * mutations里面规定的就是想要改变state(数据)的动作函数，
    * 下面的user_message 就是我将传入的message赋值给仓库中的
    * state数据字段，达到更新数据的目的
    * */
  mutations: {
    index_change (state, message) {
      state.index=message
    },
    login_in (state, id) {
      state.user_id=id
    }
  }
})
