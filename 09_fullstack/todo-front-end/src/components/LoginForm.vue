<template>
    <div class="login-form">
        <div v-if="isLoading" class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
        </div>
        <div v-else class="login-input">
            <div v-if="errors.length" class="error-list alert alert-danger">
                <h4>아래의 오류를 해결해주세요</h4>
                <ul>
                    <li v-for="(error, idx) in errors" :key="idx">{{ error }}</li>
                </ul>
            </div>
            <div class="form-group">
                <label for="username">ID</label>
                <input @keyup.enter="login" v-model="credentials.username" type="text" class="form-control" id="username"
                    placeholder="아이디를 입력해주세요">
                <!-- input에 id 써준이유는 그 위에 label 이랑 엮어주려고 한다. 현재 data에 username 없지만 credentials 만있으면 일단 된다.  -->
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input @keyup.enter="login" v-model="credentials.password" type="password" class="form-control" id="password"
                    placeholder="비밀번호를 입력해주세요">
            </div>
            <button @click="login" class="btn btn-primary">로그인</button>
        </div>
    </div>
</template>

<script>
    import router from '../router'  // router의 index.js는 알아서 찾아간다. 
    const axios = require('axios'); // 이게 es6 전에 모듈 부르는 방식 
    export default {
        name: 'LoginForm',
        data() {
            return {
                credentials: {
                    username:'',
                    password:'',
                }, // 1. id/password 에 해당하는 data
                isauthenticated: false, // 인증 여부 
                isLoading: false,
                errors: [],
            }
        },
        methods: {
            login() {
                this.isLoading = true;
                if (this.checkUserInput()) {
                    axios.post('http://localhost:8000/api-token-auth/', this.credentials)
                        .then(res => {
                            this.isLoading = false;
                            this.$sessiong.start();  // sessionStorage.session-id : sess + Date.now()
                            this.$session.set('jwt', res.data.token);
                            router.push('/');
                        })
                        .catch(err => {
                            if (!err.response) {
                                this.errors.push('Network Error...')
                            }
                            else if (err.response.status === 400) {
                                this.errors.push('Invalid username or password')
                            } else if (err.response.status === 500) {
                                this.errors.push('Internal Server error. Please try again later')
                            } else {
                                this.errors.push('Something Wrong')
                            }
                            this.isLoading = false;
                        });
                }
            
                else {
                    console.log('검증실패, 다시 작성하세요 ')
                    this.isLoading = false;
                }
            },
            checkUserInput() {
                this.errors = [];
                // 사용자가 아무말도 쓰지 않았다면
                if (!this.credentials.username) this.errors.push("username을 입력하세요.");
                if (this.credentials.password.length < 8) this.errors.push("비밀번호는 8자리 이상입니다.");
                if (!this.errors.length) return true;

            }
        }
    }
</script>

<style>

</style>