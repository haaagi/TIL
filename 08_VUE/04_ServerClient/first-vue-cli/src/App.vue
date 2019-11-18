<template>

<!-- 반드시, Templates 안에는 단 1개 의 최상단 태그 -->
<div>
    <div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">안녕안녕</div>
    <!-- <input type="text" v-model="input">
    <p>{{ filteredInput }}</p> -->
</div>
</template>

<script>
/* eslint-disable no-console */
export default {
    // name:'App',
    // // 왜인지는 모르겠지만 이제부터는 data:function() {return{}} 으로 만들어야해... 
    // data: function () {
    //     return {
    //         input: 'Type something',
    data () {
            return {
                activeColor: 'red',
                fontSize: 30
            }
        },
    //     }
    // },
    // methods: {},
    // computed: {
    //     filteredInput: function() {
    //         // [바보] 가 들어오면, ** 로 바꿔서 return 하도록 한다. 
    //         // this.result = this.input.replace('바보','**')
    //         return `Filtered:${this.input.replace(/바보|멍청이|똥개/g,'**')}`; // /바보/g 에서 g 써준 이유는 글로벌하게 다 찾아라 . gi 쓰면 대소문자 구별 안하겠다 임 
    //     }
    // }
}
</script>

<style>

</style>