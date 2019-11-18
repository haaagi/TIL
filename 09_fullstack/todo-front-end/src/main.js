import Vue from 'vue'
import App from './App.vue'
import router from './router'  // from './router/index.js' 랑 같다. 
// 이거 js는 from 뒤에있는 것들을 router에 담아주세요 라는 말이다. python 이랑 다름. 
// router안에 index.js 에서 router를 export 해줘서 그걸 가져오는거다 . 

Vue.config.productionTip = false

new Vue({
  router, // router: router,  이거랑 같은말이다. object는 키 밸류 같으면 이렇게 쓸 수 있다. 
  render: h => h(App)
}).$mount('#app')
