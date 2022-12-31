<script setup lang="ts">
import {useYukleniyorState} from "@/states/yukleniyor_state";


const yukleme = useYukleniyorState();
</script>

<template lang="pug">
div(v-if="yukleme.yukleniyor") Yükleniyor...
div(v-else-if="kargoStore.seciliKargo===null") Lütfen Bir Kişi Seçin...
div(v-else)
  .kargo-adi.metin {{ kargoStore.seciliKargo.kargo_adi }}
  .alici.metin {{ kargoStore.seciliKargo.alici }}
  .gonderici.metin {{ kargoStore.seciliKargo.gonderici }}
  .agirlik.metin {{ kargoStore.seciliKargo.agirlik }}
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

div.kargo-adi:before {
  content: '👻';
}

div.alici:before {
  content: '🏠';
}

div.gonderici:before {
  content: '📞';
}

div.agirlik:before {
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