import { createApp } from "vue";
import { createPinia } from "pinia";
// import VueGtag from "vue-gtag-next";
import { Vue3Mq, MqResponsive } from "vue3-mq";

// import solstice-vue
import SolsticeVue from "solstice-vue";

import App from "@/app.vue";
import router from "@/router";

// bootstrap-icons
import "bootstrap-icons/font/bootstrap-icons.css";

// bootstrap (all default bs styles)
// import "./css/basic.scss";

// bootstrap and solstice-vue
import "@/css/custom.scss";
import "solstice-vue/dist/style.css";

// bootstrap js (all)
import "bootstrap";

const app = createApp(App);
app.config.productionTip = false;

// vue-gtag-next
// TODO: un-commment to use Google Analytics for you app. also
// configure trackRouter located in the router/index.js file

/*
const gaCode = document.body.getAttribute("data-google-analytics");
const debugMode = document.body.getAttribute("data-django-debug");

app.use(VueGtag, {
  isEnabled: debugMode == "false",
  property: {
    id: gaCode,
    params: {
      anonymize_ip: true,
      // user_id: 'provideSomeHashedId'
    },
  },
});
*/

// vue-mq (media queries)
app.use(Vue3Mq, {
  preset: "bootstrap5",
});
app.component("mq-responsive", MqResponsive);

// pinia (vuex) state management
const pinia = createPinia();
app.use(pinia);

// solstice-vue
app.use(SolsticeVue);

// vue-router
app.use(router);

app.mount("#app");
