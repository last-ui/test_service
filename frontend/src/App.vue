<script>
import CreatePicture from "./components/CreatePicture.vue"
import PictureList from "./components/PictureList.vue";

export default {
  name: 'app',
  components: {
    'create-picture': CreatePicture,
    'picture-list': PictureList
  }
}
</script>

<template lang="pug">
#app
  section.container.grid-960
    .columns
      .column.col-2
      .column.col-8.col-md-12
        header.text-center
          h2 Create picture
        create-picture
        header.text-center
          h2 List of pictures
        picture-list
      .column.col-2
</template>

<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);
  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
