<script setup lang="ts">

const props = defineProps({
  acik: Boolean
})

</script>
<template lang="pug">
Teleport(to="body")
  Transition(name="modal")
    div.arkaplan(v-if="props.acik")
      div.modal_kapsayici
        div.modal_pencere
          div.modal_baslik
            slot(name="baslik")
              h1 Başlık
          div.modal_icerik
            slot(name="icerik")
              p İçerik
          div.modal_altbilgi
            slot(name="altbilgi")
              footer Alt bilgi
</template>
<style scoped>
div.arkaplan {
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  z-index: 9998;
  display: table;
}

div.modal_kapsayici {
  display: table-cell;
  vertical-align: middle;
  horiz-align: center;
}

div.modal_pencere {
  background-color: #7F87A2;
  width: 50%;
  margin: 0 auto;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  display: flex;
  flex-direction: column;
}

div.modal_baslik {
  padding-left: 15px;
}

div.modal_icerik {
  padding-left: 15px;
}

div.modal_altbilgi {
  padding-left: 15px;
  padding-bottom: 15px;
}

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal_kapsayici,
.modal-leave-to .modal_kapsayici {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>