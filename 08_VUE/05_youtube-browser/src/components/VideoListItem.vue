<template>
   <li @click="onVideoClick" class="list-group-item">
       <!-- alt 앞에 : 이거 붙여준 이유는 vue 가 읽을 수 있게 bind 걸어준 건다. -->
       <img :src="thumbnailUrl" class="mr-3" :alt="video.snippet.title">
       <div class="media-body">
           <span v-html="video.snippet.title"></span>
       </div>
   </li>
</template>
<script>
export default {
   name: 'VideoListItem',
   props: {
       video: Object,
   },
   methods: {
       onVideoClick () {
           this.$emit('videoSelect', this.video)
       }
   },
   // computed는 data를 수정하는건 아니고 가공해서 내보내줄 때 쓴다. 
   
   computed: {
       thumbnailUrl () {
           return this.video.snippet.thumbnails.default.url
       }
   }
}
</script>
<style scoped>
    li {
        display: flex;
        cursor: pointer;
    }
    /* 마우스 올렸을때 흐리게 하는거 */
    li:hover {
        background: #eee;
    }
</style>