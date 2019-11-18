<template>
  <div class="login">
      <h1>login page</h1>
      <LoginForm />   <!-- 이렇게 셀프 클로징으로 써도 된다. -->
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue'  // .. 은 상위폴더를 의미함. 
export default {
    name: 'Login',
    components: {
      LoginForm,
    }
}
</script>

<style>

</style>