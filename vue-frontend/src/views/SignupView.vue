<template>
    <div class="page-sign-up">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Sign Up</h1>

                <form @submit.prevent="submitForm">
                <div class="field">
                        <label>First Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="first_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Last Name</label>
                        <div class="control">
                            <input type="text" class="input" v-model="last_name">
                        </div>
                    </div>
                    <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" class="input" v-model="username">
                        </div>
                    </div>
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

                    <div class="field">
                        <label>Password Confirm</label>
                        <div class="control">
                            <input type="password" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                           <button class="button is-dark">Sign up</button>
                        </div>
                    </div>

                    <hr>
                    Or <router-link to="/login">click here </router-link> to log in!

                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignupView',
    data() {
        return {
            errors: [],
            first_name: '',
            last_name: '',
            username: '',
            email: '',
            password: '',
            password2: ''
        }
    },
    methods: {
        
        submitForm() {
            
            this.errors = [];
            console.log(this.errors)
        if(this.first_name === '') {
                this.errors.push('The first name is missing')
            }

       if(this.last_name === '') {
                this.errors.push('The last name is missing')
            }
       

            if(this.username === '') {
                this.errors.push('The username is missing')
            }
       if(this.email === '') {
                this.errors.push('The email is missing')
            }

            if(this.password === '') {
                this.errors.push('The password is missing')
            }

            if(this.password !== this.password2 ) {
                this.errors.push('The password did\'t mathch')
            }

            if(!this.errors.length) {
                console.log('no errors')
                const formData = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    username: this.username,
                    email: this.email,
                    password: this.password
                }

                axios
                .post("api/auth/register/", formData)
                .then(response => {
                    toast({
                        message: 'Account created, please log in',
                        type: 'is-success',
                        dismissible: true,
                        duration: 2000,
                        position: 'bottom-right'
                    })

                    this.$router.push('/login')
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