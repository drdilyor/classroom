<script>
import IconLink from '@/components/ui/IconLinkButton.vue'
function item(h, to, licon, content) {
  return h('li', [h(IconLink, {props: {btn: false, to: to, licon: licon}}, [
    content
  ])])
}

export default {
  functional: true,
  render(h, context) {
    return [
      h('router-link', {staticClass: 'sidenav-brand', props: {to: '/'}}, [
        '<A>code'
      ]),
      h('ul', {staticClass: 'flex-grow-1 mb-0'}, [
        item(h, '/classroom', 'home', 'Home'),
        item(h, '/courses', 'dashboard', 'Catalog'),
      ]),
      h('ul', {staticClass: 'mb-0'}, [
        item(h, '/profile', 'person','Profile'),
      ])
    ]
  }
}
</script>
<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}
li {
  padding: 1rem 3rem;
}
a {
  width: 100%;
  text-decoration: none;
  color: black;
}
.sidenav-brand {
  display: block;
  padding: .5rem 0;
  background: var(--bs-light);
  font-size: 1.6rem;
  text-align: center;
}
</style>
