import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
Vue.use(VueRouter)  // 우리 같이 일해보자. 



const router = new VueRouter({
  mode: 'history', // 원래의 브라우저 라우팅 방식 '#' 이게 없음 .  
  routes: [
    {
      path: '/',
      name: 'home',  // 이름을 home 이라고 부르겠다. 
      component: Home
    },
    {
     path: '/login',
     name: 'login',
     component: Login,  // Login 이란 컴포넌트를 뷰라우터에 보여줘라. 
    }
  ]
})

export default router
