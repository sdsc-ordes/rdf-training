<!-- A triple drawn as subject pill → predicate arrow → object pill (or dashed box for a literal). -->
<script setup lang="ts">
defineProps<{ s: string; p: string; o: string; literal?: boolean }>()
</script>

<template>
  <div class="spo">
    <span class="spo-s">{{ s }}</span>
    <span class="spo-p">{{ p }}</span>
    <span :class="literal ? 'spo-l' : 'spo-o'">{{ o }}</span>
  </div>
</template>
