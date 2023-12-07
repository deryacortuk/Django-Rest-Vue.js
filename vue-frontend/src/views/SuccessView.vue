<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank You</h1>
                <p>Payment  successfull! </p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SuccessView',
    mounted() {
        document.title = 'Success | Test'
    }
}
</script>