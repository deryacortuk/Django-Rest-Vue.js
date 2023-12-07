<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                
                <h3 class="is-size-4">{{ product.title }}</h3>
                <iframe
      width="560"
      height="315"
      :src="getEmbedUrl(product.video_file)"
      frameborder="0"
      allowfullscreen
    ></iframe>
                <p>{{ product.description }}</p>
            </div>
            
            <div class="column is-3">
                <h2 class="subtitle">Information</h2>
                <p class="is-size-6 has-text-grey">${{ product.price }}</p>
                
                <div class="field has-addons mt-6">
                    
                    <div class="control">
                        <a class="button is-dark" @click="addToCart">Add to cart</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'ProductView',
    data() {
        return {
            product: {},
            quantity: 1
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            
            const video_slug = this.$route.params.product_slug
            console.log(this.$route.params)
            await axios.get(`/api/v1/product/video/${video_slug}`)
            .then(response => {
                this.product = response.data
                document.title = this.product.title + ' | Test'
            })
            .catch( error => {
                console.log(error)
            })

            this.$store.commit('setIsLoading', false)
        },getEmbedUrl(fileUrl) {
      // Örnek: YouTube gibi farklı video sağlayıcılarının embed URL'lerini alabilirsiniz.
      // Eğer sadece dosya URL'sini kullanacaksanız doğrudan dosya URL'sini kullanabilirsiniz.
      return fileUrl;
    },
        addToCart() {
            console.log('addToCart')
            
            const item = {
                product: this.product,
                
            }
            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right'
            })
        }
    }
}
</script>