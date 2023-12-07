<template>
    <div class="page-login">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Login</h1>

                <form @submit.prevent="login">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="text" class="input" v-model="email">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                           <button class="button is-dark">Log in</button>
                        </div>
                    </div>

                    <hr>
                    Or <router-link to="/register">click here </router-link> to Sign up!

                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'


export default {
    name: "LoginView",
    data() {
        return {
            errors: [],
            email: '',
            password: ''
        }
    },
    mounted() {
        document.title = 'Login | Test Case'
    },
    methods: {
        async login() {
               
            this.errors = [];
            console.log(this.errors)


            if(this.email === '') {
                this.errors.push('The email is missing')
            }

            if(this.password === '') {
                this.errors.push('The password is missing')
            }

            if(!this.errors.length) {

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    email: this.email,
                    password: this.password
                }

                axios
                    .post("api/auth/login/", formData)
                    .then(response => {
                        const token = response.data.auth_token

                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = "Token " + token
                        localStorage.setItem("token", token)

                        const toPath = this.$route.query.to || '/cart'
                        this.$router.push(toPath)

                    })
                    .catch(error => {
                        if(error.response) {
                            for(const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }

        }
    }
}
</script>