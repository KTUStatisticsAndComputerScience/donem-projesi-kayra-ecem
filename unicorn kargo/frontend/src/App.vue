<script setup lang="ts">
import {reactive} from "vue";
import KisiListesiComponent from "@/components/KisiListesiComponent.vue";
/*
import NavbarComponent from "@/components/NavbarComponent.vue";
import BilgilerComponent from "@/components/BilgilerComponent.vue";
import AdreslerComponent from "@/components/AdreslerComponent.vue";*/
import KisiBilgileriComponent from "@/components/KisiBilgileriComponent.vue";
import AdresBilgileriComponent from "@/components/AdresBilgileriComponent.vue";

const kisi = reactive({
  kisi_adi:"",
  kisi_soyadi:"",
  tel:"",
  adres:""
});


</script>

<template>
  <div class="navbar position_absolute">
    <!--<NavbarComponent/>-->
    <a href="#"><img class="logo" src="logo.jpg" alt=""></a>
    <a href="#">Kişi İşlemleri</a>
    <a href="#">Kargo İşlemleri</a>
  </div>
  <div class="sol-taraf position_absolute">
    <KisiListesiComponent/>
  </div>
  <div class="main position_absolute">
    <!-- <BilgilerComponent/> -->
    <KisiBilgileriComponent/>
  </div>
  <div class="detay position_absolute">
    <!-- <AdreslerComponent/> -->
    <AdresBilgileriComponent/>
  </div>

</template>

<style scoped>

div.position_absolute{
  position: absolute;
}
div.navbar{
  display: flex;
  left: 0;
  top: 0;
  height: 7vh;
  width: 100vw;
  background: #7E8CB7;
  padding-top: 0;

}
/* Style the navigation bar links */
div.navbar a {
  color: white;
  padding: 24px 20px;
  text-decoration: none;
  text-align: center;
}

/* Change color on hover */
div.navbar a:hover {
  background-color: #B78C7E
;
}
div.sol-taraf{
  left: 0;
  top: 7vh;
  height: 93vh;
  width: 15vw;
  background: #8D7EB7;
  padding-left: 16px;
}
div.main{
  left: 15vw;
  top: 7vh;
  width: 85vw;
  height: 50vh;
  background: #A97EB7;
}
div.detay{
  left: 15vw;
  top: 57vh;
  width: 85vw;
  height: 43vh;
  background: #B77E8C;
}

</style>
