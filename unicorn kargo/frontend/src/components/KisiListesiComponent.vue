<script setup>
// Veri Tanımları

import {useYukleniyorState} from "@/states/yukleniyor_state";
import {useKisilerState} from "@/states/kisiler_state";
import ModalComponent from "@/components/ortak/ModalComponent.vue";
import {computed, reactive, ref} from "vue";


const yukleme = useYukleniyorState();
const kisiStore = useKisilerState();

// Veri Hazırlığı

function extracted(kisi) {
  kisiStore.seciliKisi = kisi;
}

kisiStore.yukle();

const ekleme_acik = ref(false);

const eklenecek_kisi = ref({
  kisi_adi: '',
  kisi_soyadi: '',
  tel: '',
  adres: ''
});

const ad_hatali = computed(() => {
  return eklenecek_kisi.value.kisi_adi === "";
});

const soyad_hatali = computed(() => {
  return eklenecek_kisi.value.kisi_soyadi === "";
});
/*
const tckimlik_hatali = computed(() => {
  return eklenecek_kisi.value.tckimlik === "" || eklenecek_kisi.value.tckimlik.length !== 11;
});

const dogum_tarihi_hatali = computed(() => {
  return eklenecek_kisi.value.dogumtarihi === "";
});
*/
const tel_hatali = computed(() => {
  return eklenecek_kisi.value.tel === "";
});

const adres_hatali = computed(() => {
  return eklenecek_kisi.value.adres === "";
});

const kaydet_aktif = computed(() => {
  return !(ad_hatali.value || soyad_hatali.value || tel_hatali.value || adres_hatali.value);
});

/*const hatalar = reactive({
  ad_hatali: false,
  soyad_hatali: false,
  tckimlik_hatali: false,
  dogum_tarihi_hatali: false
});*/

/*function kontrol_et() {
  if (eklenecek_kisi.value.ad === "") {
    hatalar.ad_hatali = true;
  }
  if (eklenecek_kisi.value.soyad === "") {
    hatalar.soyad_hatali = true;
  }
  if (eklenecek_kisi.value.tckimlik === "" || eklenecek_kisi.value.tckimlik.length !== 11) {
    hatalar.tckimlik_hatali = true;
  }
  if (eklenecek_kisi.value.dogum_tarihi === "") {
    hatalar.dogum_tarihi_hatali = true;
  }
  return hatalar.ad_hatali || hatalar.soyad_hatali || hatalar.tckimlik_hatali || hatalar.dogum_tarihi_hatali;
}*/

function kaydet() {
  kisiStore.ekle(eklenecek_kisi.value);
  iptal();
}

function iptal() {
  eklenecek_kisi.value.kisi_adi = "";
  eklenecek_kisi.value.kisi_soyadi = "";
  eklenecek_kisi.value.tel = "";
  eklenecek_kisi.value.adres = "";
  ekleme_acik.value = false;
}


</script>

<template lang="pug">
button.yeni-kisi(v-if="!yukleme.yukleniyor && kisiStore.kisiListesi.length>0", @click="ekleme_acik=true") ➕
div(v-if="yukleme.yukleniyor")
  span.loader
  span Yükleniyor
div(v-else-if="kisiStore.kisiListesi.length===0") Kişi Bilgileri Bulunamadı!
div(v-else, v-for="kisi_listesi in kisiStore.kisiListesi")
  .baslik(v-if="kisi_listesi.kisiler.length>0")
    h1 {{ kisi_listesi.harf }}
  .kisi(v-if="kisi_listesi.kisiler.length>0", v-for="kisi in kisi_listesi.kisiler", @click="kisiStore.seciliKisi=kisi")
    a {{ kisi.kisi_adi }} {{ kisi.kisi_soyadi }}
button(@click="kisiStore.yukle()", :disabled="yukleme.yukleniyor") Yenile
ModalComponent(:acik="ekleme_acik")
  template(#baslik)
    div.ekleme_baslik
      h1 Yeni Kişi Ekle
      button.kapat(@click="iptal") ➕
  template(#icerik)
    div.form
      label(for="isim") Kişi İsmi
      input(type="text", name="isim", id="isim", v-model="eklenecek_kisi.kisi_adi")
      span.hata(v-if="ad_hatali") Ad Bilgisini Düzeltin
      label(for="soyisim") Kişi Soyismi
      input(type="text", name="soyisim", id="soyisim", v-model="eklenecek_kisi.kisi_soyadi" )
      span.hata(v-if="soyad_hatali") Soyad Bilgisini Düzeltin
      label(for="tel") Telefon
      input(type="text", name="tckimlik", id="tckimlik", v-model="eklenecek_kisi.tel" )
      span.hata(v-if="tel_hatali") Telefon Bilgisini Düzeltin
      label(for="adres") Adres
      input(type="text", name="dogumtarihi", id="dogumtarihi", v-model="eklenecek_kisi.adres" )
      span.hata(v-if="adres") Adres Bilgisini Düzeltin
  template(#altbilgi)
    div.butonlar
      button.kaydet(@click="kaydet")
        span.simge ➕
        span.metin Kaydet
      button.iptal(@click="iptal")
        span.simge &times;
        span.metin İptal
</template>
<style scoped>

span.hata {
  color: red;
  font-size: 9pt;
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: black;
  margin-bottom: 10px;
}

button.kaydet {
  background-color: #00A36C;
  color: white;
  font-weight: bold;
  padding: 10px;
  border: black solid 1px;
}

button.iptal {
  background-color: #FF4433;
  color: white;
  font-weight: bold;
  padding: 10px;
  border: black solid 1px;
}

div.butonlar {
  display: flex;
  flex-direction: row-reverse;
  width: 90%;
}

div.butonlar button {
  margin-left: 5px;
}

button.iptal span.simge {
  transform: rotate(45deg);
}

div.form {
  display: flex;
  flex-direction: column;
  width: 90%;
  margin-bottom: 10px;
}

div.ekleme_baslik {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

button.kapat {
  margin-top: 15px;
  margin-right: 15px;
  background-color: #7F87A2;
  border: none;
  cursor: pointer;
  transform: rotate(45deg);
}

div.baslik {
  border-bottom: 1px solid black;
}

div.kisi {
  width: 100%;
  height: 50px;
  margin: 0;
  padding: 10px 0 0 10px;
  cursor: pointer;
  border: 1px solid transparent;
}

div.kisi:hover {
  background: #7F8186;
  border: 1px dot-dash black;
}

button.yeni-kisi {
  position: fixed;
  bottom: 3px;
  width: 13vw;

}

.loader {
  width: 48px;
  height: 48px;
  border: 5px solid #FFF;
  border-bottom-color: transparent;
  border-radius: 50%;
  display: inline-block;
  box-sizing: border-box;
  animation: rotation 1s linear infinite;
}

@keyframes rotation {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

</style>