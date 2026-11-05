<!-- A word in a competency question, marked once the slide reaches the click for its kind (1 class, 2 property, 3 value, 4 literal). -->
<script setup lang="ts">
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps<{ k: 'class' | 'property' | 'value' | 'literal' }>()
const STEP = { class: 1, property: 2, value: 3, literal: 4 }
const { $clicks } = useSlideContext()
const on = computed(() => $clicks.value >= STEP[props.k])
</script>

<template>
  <span class="term" :class="[`term-${k}`, { on }]"><slot /></span>
</template>
