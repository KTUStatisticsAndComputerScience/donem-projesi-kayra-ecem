import {defineStore} from "pinia";
import {useYukleniyorState} from "@/states/yukleniyor_state";
import axios from "axios";

export const useKisilerState = defineStore('kisiler', {
    state: () => ({
        kisiler: [],
        kisiListesi: [],
        seciliKisi: null
    }),
    actions: {
        yukle() {
            const yukleme = useYukleniyorState();
            yukleme.yuklemeyeBasla();
            this.seciliKisi = null;
            axios.get("kisi/")
                .then((response)=>{
                    this.kisiler = response.data;
                    this.grupla();
                    yukleme.yuklemeyiBitir();
                });
        },
        ekle(kisi) {
            axios.post('kisi/', kisi)
                .then((response) => {
                    const kisi = response.data;
                    this.kisiler.push(kisi);
                    const harf = kisi.kisi_adi[0];
                    this.kisiListesi.forEach((alt_liste) => {
                        if(alt_liste.harf===harf) {
                            alt_liste.kisiler.push(kisi);
                        }
                    })
                })
        },
        sirala() {
        },
        grupla() {
            const ilkHarfler = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'H', 'I',
                'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R',
                'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z'];
            this.kisiListesi = [];
            ilkHarfler.forEach((h) => {
                this.kisiListesi.push({
                    harf: h,
                    kisiler: this.kisiler.filter((kisi) => {
                        if (kisi.kisi_adi.toUpperCase().startsWith(h)) {
                            return true;
                        }
                        return false;
                    })
                });
            });
        },
        arama() {
        }
    }
});