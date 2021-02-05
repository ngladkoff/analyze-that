<template>
  <div>
    <CRow>
      <CCol>
        <CButton color="primary" variant="outline" class="m-2" @click="newGame">Nuevo Juego</CButton>
      </CCol>
    </CRow>
    <div style="padding:10px;"></div>
    <CRow>
      <CCol col="12" sm="6" lg="6">
        <CWidgetIcon
          header="Scrum Game"
          text="Juego para enseñanza de Scrum"
          color="primary"
          :icon-padding="false"
        >
          <CIcon name="cil-casino" width="24"/>
          <template #footer>
            <CCardFooter class="card-footer px-3 py-2">
              <CLink
                class="font-weight-bold font-xs btn-block text-muted"
                href="https://coreui.io/"
              >
                Ver mas
                <CIcon name="cil-arrowRight" class="float-right" width="16"/>
              </CLink>
            </CCardFooter>
          </template>
        </CWidgetIcon>
      </CCol>
      <CCol col="12" sm="6" lg="6">
        <CWidgetIcon
          header="Platform Game"
          text="Juego de plataforma para medición de variables psicológicas"
          color="primary"
          :icon-padding="false"
        >
          <CIcon name="cil-running" width="24"/>
          <template #footer>
            <CCardFooter class="card-footer px-3 py-2">
              <CLink
                class="font-weight-bold font-xs btn-block text-muted"
                href="https://coreui.io/"
              >
                Ver mas
                <CIcon name="cil-arrowRight" class="float-right" width="16"/>
              </CLink>
            </CCardFooter>
          </template>
        </CWidgetIcon>
      </CCol>

    </CRow>

  </div>
</template>

<script>

export default {
  name: 'GamesData',
  components: {
  },
  data () {
    return {
    }
  },
  methods: {
    newGame() {
      this.$router.push({ path: 'new'})
    }
  }
}
</script>
