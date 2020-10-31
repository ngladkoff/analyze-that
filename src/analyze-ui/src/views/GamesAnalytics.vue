<template>
  <div>
    <CRow>
      <CCol sm="6" lg="3">
        <CWidgetDropdown 
            color="primary" 
            header="Scrum Game" 
            text="Juego para enseñanza de Scrum">
          <template #default>
            <CDropdown
              color="transparent p-0"
              placement="bottom-end"
            >
              <template #toggler-content>
                <CIcon name="cil-chart-line"/>
              </template>
              <CDropdownItem>Nuevo Análisis</CDropdownItem>
              <CDropdownItem>Ver Análisis</CDropdownItem>
            </CDropdown>
          </template>
          <template #footer>
            <div style="padding:10px;"></div>
          </template>
        </CWidgetDropdown>
      </CCol>
      <CCol sm="6" lg="3">
        <CWidgetDropdown 
            color="primary" 
            header="Platform Game" 
            text="Juego de plataforma para medición de variables psicológicas">
          <template #default>
            <CDropdown
              color="transparent p-0"
              placement="bottom-end"
            >
              <template #toggler-content>
                <CIcon name="cil-chart-line"/>
              </template>
              <CDropdownItem>Nuevo Análisis</CDropdownItem>
              <CDropdownItem>Ver Análisis</CDropdownItem>
            </CDropdown>
          </template>
          <template #footer>
            <div style="padding:10px;"></div>
          </template>
        </CWidgetDropdown>
      </CCol>
    </CRow>
  </div>
</template>

<script>

export default {
  name: 'GamesAnalytics',
  components: {
  },
  data () {
    return {
    }
  },
  methods: {
  }
}
</script>
