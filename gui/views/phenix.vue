<script setup>
import { inject, onMounted, ref } from "vue";

const $api = inject("$api");

const name = ref('');
const description = ref('');
const planners = ref([]);

onMounted(async () => {
    const response = await $api.get('/plugin/phenix/data')
    const pluginData = await response.data

    name.value = pluginData.name
    description.value = pluginData.description
    planners.value = pluginData.planners
});

function handleBoxExit(e){
    e.target.scrollTo({top: 0, behavior: 'smooth'});
}
</script>

<template>
    <div>
        <h2>{{ name }} Plugin</h2>
        <p>{{ description }}</p>
    </div>
    <hr>

    <h3>Documentation</h3>
    <p>
        Get started by referencing the
        <a
          :href="`/docs/plugins/${name.toLowerCase()}/${name.toLowerCase()}.html`" target="_blank">{{ name }} Plugin Field Manual</a>.
    </p>

    <h3>Planners</h3>
    <div class="columns planners is-multiline">
        <div v-for="p in planners" class="column is-one-quarter p-1 m-0">
            <div class="box otbox p-3 m-1" @mouseleave="handleBoxExit">
                <div class="inner_otbox">
                    <div>
                        <span class="has-text-weight-bold">{{p.name}}</span>
                    </div>
                    <div class="help mb-0">{{p.description}}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
h2 {
    font-size: 1.75rem;
    line-height: 1.75rem;
    font-weight: 800;
    padding: 1rem 0;
}
h3 {
    font-size: 1.5rem;
    line-height: 1.75rem;
    font-weight: 800;
    padding: 1rem 0;
}
hr {
    margin: 1rem 0;
}
p {
    padding: 0 0 1rem 0;
}
a {
    color: #D6B8EF; 
}
a:hover {
    color: #8b00ff; 
}
.otbox{
    height: 200px;
    background-color: rgba(139, 0, 255, 0.4); 
    overflow-y: hidden;
    overflow-x: wrap;
}
.otbox:hover{
    outline: 3px;
    outline-color: #8B00FE; 
    background-color: rgba(139, 0, 255, 0.7); 
    outline-style: solid;
    overflow-y: scroll;
}
.inner_otbox{
    margin-right: 15px;
}
</style>
