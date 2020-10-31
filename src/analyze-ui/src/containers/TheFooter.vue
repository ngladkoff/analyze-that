<template>
  <CFooter :fixed="false">
    <div>
      <a href="https://uade.edu.ar" target="_blank">UADE</a>
      <span class="ml-1">&copy; {{new Date().getFullYear()}} Nicol&aacute;s A. Gladkoff.</span>
    </div>
    <!-- <div class="ml-auto">
      <span class="mr-1">Powered by</span>
      <a href="https://coreui.io/vue" target="_blank">CoreUI for Vue</a>
    </div> -->
  </CFooter>
</template>

<script>
export default {
  name: 'TheFooter'
}
</script>
