<template>
  <amplify-authenticator username-alias="email">
    <amplify-sign-up slot="sign-up" username-alias="email" :form-fields.prop="signInUpFields"></amplify-sign-up>
    <amplify-sign-in slot="sign-in" username-alias="email" :form-fields.prop="signInUpFields"></amplify-sign-in>
    <router-view></router-view>
    <!-- <amplify-sign-out></amplify-sign-out> -->
  </amplify-authenticator>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      signInUpFields: [
        {
          type: 'email',
          label: 'Email:',
          placeholder: 'Ingrese su email',
          required: true,
        },
        {
          type: 'password',
          label: 'Contraseña:',
          placeholder: 'Ingrese su contraseña',
          required: true,
        },
      ]
    }
  }
}
</script>

<style lang="scss">
  // Import Main styles for this application
  @import 'assets/scss/style';
</style>
