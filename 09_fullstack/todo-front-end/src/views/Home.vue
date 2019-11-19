<template>
  <div class="home">
    <h1>This is Home</h1>
  </div>
</template>

<script>
import router from '../router';
// @ is an alias to /src
export default {
  name: 'home',
  methods: {
    isLoggedIn () {
      this.$session.start();
      if (!this.$session.has('jwt')) { // jwt 가 없으면 ( 로그인 안했으면 )
        router.push('/login');
      }
    }
  },
  created () {  // 이거 beforeCreated 는 안된다. vue life cycle 확인해서 써주자 ! ! ! ! ! ! ~! ! ! ! ! ! ! 
    this.isLoggedIn()
  }
}
</script>
