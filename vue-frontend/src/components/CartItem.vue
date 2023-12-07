<template>
    <tr>
        <td><router-link :to="item.product.get_absolute_url">{{ item.product.title}}</router-link></td>
      
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
        <td><button class="delete" @click="removeFromCart(item)">-</button></td>

    </tr>    
</template>

<script>
export default {
    name: 'CartItem',
    props: {
        initialItem: Object 
    },
    data() {
        return {    
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.product.quantity * item.product.price
        },
        
        updateCart() { 
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item) 
            this.updateCart()
        },
    }
}
</script>