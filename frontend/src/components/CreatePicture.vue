<template lang="pug">
p.text-error(v-if="errors.length" v-for="error in errors") {{ error }}
form.form-horizontal(@submit="submitForm")

  .form-group
    .col-3
      label.form-label Description
    .col-9
      input.form-input(type="text" v-model="description" placeholder="Type picture description...")
  .form-group
    .col-3
      label.form-label Image File
    .col-9
      input.form-input(type="file" v-on:change="createBase64Image" accept="image/*" ref="fileupload")
      textarea.form-input(v-model="base64textString" rows=8 style="display:none;")
  .form-group
    .col-3
    .col-9
      button.btn.btn-primary(type="submit") Create
</template>
<script>
export default {
  name: 'create-picture',
  data () {
    return {
      'description': '',
      'base64textString': '',
      'errors': []
    }
  },
  methods: {
    checkForm: function (event) {
        this.errors = [];
        if (this.description === '' || this.$refs.fileupload.value === '') {
          this.errors.push( "All fields are required." );
        } else { this.createPicture() }
    },
    createBase64Image: function (event) {
        const file = event.target.files[0];
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            this.base64textString = reader.result;
        };
    },
    submitForm (event) {
      this.checkForm();
      this.description = '';
      this.base64textString = '';
      this.$refs.fileupload.value = null;
      event.preventDefault()
    },
    createPicture () {
      this.$store.dispatch('createPicture', { description: this.description, image: this.base64textString })
    }
  }
}
</script>
