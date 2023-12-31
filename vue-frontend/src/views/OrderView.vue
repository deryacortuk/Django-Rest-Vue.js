<template>
    <div class="page-checkout">
        <div class="columns is-multiline">

            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>-</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    
                    <tbody>
                        <tr v-for="item in cart.items" v-bind:key="item.product.id">
                            <td>{{ item.product.title }}</td>
                            <td>{{ item.product.price }}</td>
                            <td>{{ item.product.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td></td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>

                </table>
            </div>


            <div class="column is-12">
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-grey mb-4">* All fields are required</p>
               
                <div class="columns is-multiline">
                    
                    <div class="column is-6">
                        <div class="field">
                            <label>First Name*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last Name*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address*</label>  
                            <div class="control">
                                <textarea class="input" v-model="address"></textarea>
                            </div>
                        </div>
                        <div class="field">
                            <label>Zipcode*</label>  
                            <div class="control">
                                <input class="input" v-model="zipcode">
                            </div>
                        </div>
                      
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
                <hr>
                
                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalPrice">
                    <hr>
                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'OrderView',
    data() {
        return { 
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',           
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Ecommerce Store'

        this.cart = this.$store.state.cart

        
        if(this.cartTotalLength > 0) {
            this.stripe = Stripe('pk_test_51MsQVNKp6OR8SiixfcRdzvgHfF1UvK6m2YTdKeNjEAaqiGB8j3Unq9yZ5ssGzXTJTOb2HEfkUY8PnmQr1yyJCmJ9001ZtK4ABU') 
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })

            this.card.mount('#card-element')
        }
    },
    methods: {
        getItemTotal(item) {
            return 1 * item.product.price
        },
        submitForm() {
            this.errors = []

            if(this.first_name === '') {
                this.errors.push('The first name field is required')
            }

            if(this.last_name === '') {
                this.errors.push('The last name field is required')
            }

            if(this.email === '') {
                this.errors.push('The email field is required')
            }

            if(this.phone === '') {
                this.errors.push('The phone field is required')
            }

            if(this.phone === '') {
                this.errors.push('The phone field is required')
            }

            if(this.address === '') {
                this.errors.push('The address field is required')
            }

            if(this.zipcode === '') {
                this.errors.push('The zipcode field is required')
            }

            if(this.place === '') {
                this.errors.push('The place field is required')
            }

            // if has not errors
            if(!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                
                // stripe toke creator
                this.stripe.createToken(this.card).then( result => {
                    if(result.error) {
                        this.$store.commit('setIsLoading', false)

                        this.errors.push('Something went wrong with Stripe. Please try again')

                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token) // ajax call
                    }
                })

            }
        },

        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++ ) {
                const item = this.cart.items[i]

                // order items
                const obj = {
                    product: item.product.id,
                    quantity: item.product.quantity,
                    price: item.product.price * item.product.quantity
                }

                items.push(obj)
            }

            // order object
            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,                
                'phone': this.phone,
                'items': items,
                'stripe_id': token.id
            }

            // ajax post request
            await axios
                .post('/api/v1/payment/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)

        }

    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.product.price * 1
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.forEach((acc, currentValue) => {
              console.log(currentValue.quantity)
                return acc += currentValue.quantity
                
            }, 0)
        }
    }
}
</script>