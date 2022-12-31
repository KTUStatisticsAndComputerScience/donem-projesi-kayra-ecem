import {defineStore} from "pinia";


export const useYukleniyorState = defineStore('yukleniyor',
    {
        state: () => ({yukleniyor: false}),
        actions: {
            yuklemeyeBasla() {
                this.yukleniyor = true;
            },
            yuklemeyiBitir() {
                this.yukleniyor = false;
            }
        },
    });