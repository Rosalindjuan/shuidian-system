<template>
  <div id="app">
    <router-view/>
    <v-toast></v-toast>
  </div>
</template>

<script>
  import VToast from '@/components/common/toast.vue'
export default {
  name: 'App',
  components: {
    VToast
  }
}
</script>

<style>
  @import "../static/css/main.css";
  @import "../static/css/color-dark.css";     /*深色主题*/
  @import "../static/css/common.css";
</style>
