// home.vue

<template>
  <layout :page-title="pageTitle">
    <!-- page content -->
    <template #title>
      {{ pageTitle }}
    </template>

    <template #description>
      <div class="p-0 col-md-8 lead">
        <p>
          <a href="https://github.com/uw-it-aca/axdd-django-vue"
            >AXDD-Django-Vue</a
          >
          is a high-opinionated template repository created and used by AXDD to
          make our build processes consistent and repeatable through established
          patterns across our CICD architecture.
        </p>

        <HelloWorld />
      </div>
    </template>

    <template #content>
      <div class="row">
        <div class="col-md-6">
          <h2>Requirements</h2>
          <p>Download the following:</p>
          <ul>
            <li>
              <a
                href="https://www.docker.com/products/docker-desktop/"
                target="_blank"
                >Docker Desktop
              </a>
              (4.18.0)
            </li>
            <li>
              <a href="https://nodejs.org/en" target="_blank">NodeJS</a>
              (18.16.0 LTS)
            </li>
          </ul>

          <h2>Development</h2>
          <p>
            What's included? This template repository is intended to start you
            off with AXDD's supported development stack.
          </p>
          <ul>
            <li>Django (3.2.8)</li>
            <li>Vue (3.3.1)</li>
            <li>Vite (4.3.5)</li>
          </ul>

          <h2>Design</h2>
          <ul>
            <li>Bootstrap (5.2.0)</li>
            <li>Bootstrap Icons (1.9.0)</li>
          </ul>
        </div>
        <div class="col-md-6">
          <h2>Testing</h2>
          <ul>
            <li>
              <a href="https://vitest.dev/" target="_blank">Vitest (0.28.5)</a>
            </li>
            <li>
              <a href="https://test-utils.vuejs.org/" target="_blank"
                >Vue Test Utils (2.3.0)</a
              >
            </li>
          </ul>

          <h2>Linting (code quality)</h2>
          <ul>
            <li>Pycodestyle for Python</li>
            <li>ESLint for JS</li>
            <li>Stylelint for CSS</li>
          </ul>

          <h2>AXDD Libraries</h2>
          <p>
            The following is a list of specific AXDD libraries used in building
            applications.
          </p>
          <ul>
            <li>
              <a
                href="https://github.com/uw-it-aca/django-container"
                target="_blank"
                >Django-Container (1.4.1)</a
              >
            </li>
            <li>
              <a
                href="https://github.com/uw-it-aca/axdd-components"
                target="_blank"
                >AXDD-Components (1.0.6)</a
              >
            </li>
          </ul>
        </div>

        <hr />

        <div class="col-md-6">
          <h2>Libraries</h2>
          <p>
            The following is a list of common JS and Vue libraries included in
            this repository.
          </p>
          <ul>
            <li>
              <a href="https://axios-http.com/" target="_blank">axios</a> (data
              fetching)
            </li>
            <li>
              <a href="https://pinia.vuejs.org/" target="_blank">pinia</a>
              (state management, formerly vuex)
            </li>
            <li>
              <a
                href="https://matteo-gabriele.gitbook.io/vue-gtag/v/next/"
                target="_blank"
                >vue-gtag-next</a
              >
              (google analytics)
            </li>
            <li>
              <a href="https://github.com/KanHarI/vue3-cookies" target="_blank"
                >vue3-cookies</a
              >
              (cookies)
            </li>
            <li>
              <a href="https://github.com/craigrileyuk/vue3-mq" target="_blank"
                >vue3-mq</a
              >
              (css media queries)
            </li>
          </ul>
        </div>
      </div>
    </template>
  </layout>
</template>

<script>
import Layout from "@/layout.vue";
//import HelloWorld from "@/components/hello-world.vue";

export default {
  name: "PagesHome",
  components: {
    layout: Layout,
    //HelloWorld,
  },
  data() {
    return {
      pageTitle: "Getting started",
    };
  },
  methods: {},
};
</script>
