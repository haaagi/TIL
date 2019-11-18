<template>
    <div>
        <!-- ()는 커스텀 인자 없으면 안붙임 -->
        <!-- v-on 을 줄여서 @ -->
        <!-- methods 는 내가 인자를 넘긴다면 (ARG) 붙이고 -->
        <!-- 그게 아니라면 () 안붙임 -->
        <!-- <input @input="onInput" type="text"> -->
        <input @keypress.enter="onInput" type="text">
    </div>
</template>

<script>
export default {
    name: 'SearchBar', // new component 0. 이름적기
    methods: {
        onInput (e) {
            // this.$ 이거는 특수한 애들이 몇개 있는데 emit() 은 이거 함수가 이미 정의되있음. 
            // this.$emit('Event 이름','전송할 값') : 자식 component, => 부모 component 정보 (데이터)를 올려보낼때 쓴다. 
            this.$emit('inputChange',e.target.value)
            
        }
    }
    
}
</script>

<style scoped>
/* scoped: 해당 컴포넌트의 태그들만 영향을 받는다.  */
    input {
        width:75%;
    }
    div {
        text-align: center;
        margin: 20px;
    }
</style>