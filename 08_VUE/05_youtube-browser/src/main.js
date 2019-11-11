import Vue from 'vue';
// import 되는 이유는 App 에 export default 를 써주었기 때문에 그 코드를 읽는다. 
import App from './App'; // App.vue 가 아닌 이유는 알아서 확장자 떼고 읽는다. 

new Vue({
    // el: '#app',
    render: (h) => h(App), // 유일하게 method인데 arrow funtion 이다. 
}).$mount('#app')  //이거 mount 쓰는 이유는 el 저거 안써주려고 쓰는거다. 이거를 더 많이 쓰나보다. 