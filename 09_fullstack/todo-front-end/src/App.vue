<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
      <!-- login 누르면 index.js에서 LoginForm 을 보여줘라 를 실행하고 그걸 routerview 로 보여줘라. -->
    </div>
    <div class="container col-6">
      <router-view/>  <!-- 다른 url 이 들어오면 여기서 보여주세요 -->
    </div>
    
  </div>
</template>

<style>

</style>
