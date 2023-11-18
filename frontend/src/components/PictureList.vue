<script>
import { mapGetters } from 'vuex'
export default {
  name: 'picture-list',
  computed: mapGetters(['pictures']),
  methods: {
    deletePicture (picture) {
      this.$store.dispatch('deletePicture', picture)
    }
  },
  beforeMount () {
    this.$store.dispatch('getPictures')
  }
}
</script>
<template lang="pug">
#app
  .card(v-for="picture in pictures" v-bind:key="picture.id")
    .card-header
      button.btn.btn-clear.float-right(@click="deletePicture(picture)")
      .card-title {{ picture.description }}
    img(v-bind:src="picture.image"  width="150")
</template>

<style>
  header {
    margin-top: 50px;
  }
</style>
