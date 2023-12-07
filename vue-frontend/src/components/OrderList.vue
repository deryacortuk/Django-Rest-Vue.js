<template>
    <div class="box mb-4">
        <h3 class="is-size-4 mb-6">Order #{{ order.id }}</h3>

        <h4 class="is-size-5">Products</h4>

        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <td>Product</td>
                    <td>Price</td>                   
                    <td>Total</td>
                </tr>
            </thead>

            <tbody>
                <tr v-for="item in order.items" v-bind:key="item.product.id">
                    <td>{{ item.product.title }}</td>
                    <td>{{ item.product.price }}</td>                    
                    <td>${{ getItemTotal(item).toFixed(2) }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    name: 'OrderList',
    props: {
        order: Object
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        orderTotalLength(order) {
            return order.items.reduce( (acc, currentVal) => {
                return acc += currentVal.quantity
            }, 0)
        }
    }
}
</script>