<script setup lang="ts">
import {useYukleniyorState} from "@/states/yukleniyor_state.js";
import {useKisilerState} from "@/states/kisiler_state.js";


const yukleme = useYukleniyorState();
const kisiStore = useKisilerState();
</script>

<template lang="pug">
div(v-if="yukleme.yukleniyor") Yükleniyor...
div(v-else-if="kisiStore.seciliKisi===null") Lütfen Bir Kişi Seçin...
div(v-else)
  .ad-soyad.metin {{ kisiStore.seciliKisi.kisi_adi }} {{ kisiStore.seciliKisi.kisi_soyadi }}
  .adres.metin {{ kisiStore.seciliKisi.adres }}
  .tel.metin {{ kisiStore.seciliKisi.tel }}
  button.duzenle ✒️
  button.sil 🗑️
</template>

<style scoped>

div.metin {
  font-family: Corbel;
  box-sizing: border-box;
  padding: 10px 10px 10px 10px;
  font-size: 36pt;
}

div.ad-soyad:before {
  content: '👻';
}

div.adres:before {
  content: '🏠';
}

div.tel:before {
  content: '📞';
}

button {
  border: black solid 1px;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  font-size: 24pt;
}

button.duzenle {
  background: deepskyblue;
  position: absolute;
  right: 80px;
  bottom: 25px;
}

button.sil {
  background: deeppink;
  position: absolute;
  right: 10px;
  bottom: 25px;
}

</style>