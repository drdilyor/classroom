<template>
  <div class="toggler" :class="{on}" @click="$emit('click', $event)">
    <div class="bar bar-1"></div>
    <div class="bar bar-2"></div>
    <div class="bar bar-3"></div>
  </div>
</template>

<script>
export default {
  props: {
    on: {
      type: Boolean,
      default: true,
    }
  },
}
</script>

<style scoped>
.toggler {
  position: relative;
  width: 32px;
  height: 20px;
  cursor: pointer;
}
.bar {
  position: absolute;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--bs-gray);
  transition: all .3s;
}

.bar-1 { top: 0 }
.bar-3 { bottom: 0 }
.bar-2 {
  top: 50%;
  transform: translateY(-50%);
}

.on .bar-1 {
  top: 50%;
  transform: translateY(-50%) rotate(45deg);
}
.on .bar-2 {
  opacity: 0;
}
.on .bar-3 {
  top: 50%;
  transform: translateY(-50%) rotate(-45deg);
}
</style>
