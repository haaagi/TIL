<template>
<!-- 이 template 안에는 div가 하나여야만 된다. 뭐 다른 div나 p 태그 넣으면 오류 나온다. -->
<!-- div태그 안에는 많이 넣어도 됌. -->
    <div class="container">
        <!-- 3. template 에 보여주기  -->
        <SearchBar @inputChange="onInputChange"></SearchBar>
        <div class="row">
             <!--  v-on:[자식 component에서 emit 하는 이벤트 이름]="" -->
            <VideoDetail :video="selectedVideo"></VideoDetail>
            <!-- v-bind 는 줄여서 ':' 이거로 쓴다.  -->
            <!-- props 사용하기  step 0. bind 로 데이터를 넘긴다.  -->
            <VideoList 
                :videos="videos"
                @videoSelect="onVideoSelect"
            >
            </VideoList>
            <div class="static" v-bind:class="{ active: isActive, error: hasError }"></div>
        </div>

    </div>
</template>

<script>
    
    import SearchBar from './components/SearchBar'; // 1. import 하기 
    import VideoList from './components/VideoList';
    import VideoDetail from './components/VideoDetail';
    import axios from 'axios';
    const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;
    export default {
        // 컴포넌트를 생성하면
        // 0. 이름적기
        name: 'App',
        components: {
            SearchBar, // 2. 부모에게 자식들 등록하기 
            VideoList,
            VideoDetail,
        },
        data () {
            return {
                videos: [], // 이거 처음에 빈 값이라도해도 이렇게 선언해줘야 한다. 
                selectedVideo: null,
                isActive: true,
                hasError: false,
            }
        },
        methods: {
            onInputChange (inputValue) {
                axios.get('https://www.googleapis.com/youtube/v3/search', {
                    params: {
                        key: API_KEY,
                        type: 'video',
                        part: 'snippet',
                        q: inputValue,
                    }
                })
                .then(res => this.videos = res.data.items)
            },
            onVideoSelect (video) {
                this.selectedVideo = video
            }
        },
    }
</script>

<style>
    
</style>