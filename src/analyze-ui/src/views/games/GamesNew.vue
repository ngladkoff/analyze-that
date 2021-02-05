<template>
  <div>
    <CRow>
      <CCol>
      <CCard>
        <CCardHeader>
          <CIcon name="cil-pencil"/> <strong>Nuevo Juego</strong>
        </CCardHeader>
        <CCardBody>
          <CForm>
            <CInput
              label="Nombre del juego"
              required
            />
            <CInput
              label="Descripción"
              required
            />
            <CTextarea
              label="Observaciones"
              placeholder=""
              rows="9"
            />
            <CCard>
              <CCardHeader>
                <strong>Icono</strong> <small>Seleccione un icono para el juego</small>
              </CCardHeader>
              <CCardBody>
                <CRow>
                  <CCol>
                    <CListGroup>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center" active><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                    </CListGroup>
                  </CCol>
                  <CCol>
                    <CListGroup>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center" active><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                    </CListGroup>
                  </CCol>
                  <CCol>
                    <CListGroup>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center" active><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                    </CListGroup>
                  </CCol>
                  <CCol>
                    <CListGroup>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center" active><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                    </CListGroup>
                  </CCol>
                  <CCol>
                    <CListGroup>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center" active><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                      <CListGroupItem class="text-center"><CIcon name="cil-pencil"/></CListGroupItem>
                    </CListGroup>
                  </CCol>

              </CRow>
              </CCardBody>
            </CCard>
          </CForm>
        </CCardBody>
        <CCardFooter>
          <CButton type="submit" size="sm" color="primary"><CIcon name="cil-save"/> Guardar</CButton>
        </CCardFooter>
      </CCard>
      </CCol>
    </CRow>
  </div>
</template>

<script>

export default {
  name: 'GamesDataNew',
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
