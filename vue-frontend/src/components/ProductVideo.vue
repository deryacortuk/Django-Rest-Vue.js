<template>
    <div class="column is-4">
        <div class="box">
            
            <iframe
      width="315"
      height="315"
      :src="getEmbedUrl(product.video_file)"
      frameborder="0"
      allowfullscreen
    ></iframe>
            <h3 class="is-size-4">{{ product.title }}</h3>            
            <p class="is-size-6 has-text-grey">${{ product.price }}</p>
     

            <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Detail</router-link>

        </div>
    </div>
</template>

<script>
export default {
    name: 'ProductVideo',
    props: { 
        product: Object
    }, 
    methods:{
        getEmbedUrl(fileUrl) {
      // Örnek: YouTube gibi farklı video sağlayıcılarının embed URL'lerini alabilirsiniz.
      // Eğer sadece dosya URL'sini kullanacaksanız doğrudan dosya URL'sini kullanabilirsiniz.
      return fileUrl;
    },
    }
}

</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>