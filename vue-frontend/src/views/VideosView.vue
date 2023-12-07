<template>
  <div class="page-all-products">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-3 has-text-centered">All Products</h2>
      </div>

      <ProductVideo
        v-for="product in allProducts"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ProductVideo from '@/components/ProductVideo'

export default {
  name: 'VideosView',
  components: {
    ProductVideo
  },
  data() {
    return {
      allProducts: []
    }
  },
  
  mounted() {
    this.getAllProducts()
  },
  methods: {
    async getAllProducts() {
      this.$store.commit('setIsLoading', true)

      try {
        const response = await axios.get('/api/v1/product/videos/')
        this.allProducts = response.data

        document.title = 'All Products | Online Tutorial'
      } catch (error) {
        console.error(error)

        toast({
          message: 'Something went wrong. Please try again.',
          type: 'is-danger',
          dismissible: true,
          pauseOnHover: true,
          duration: 2000,
          position: 'bottom-right'
        })
      }

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>
