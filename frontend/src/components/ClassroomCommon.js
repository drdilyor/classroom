export default {
  mounted() {
    // initialize sidenav
    const elems = document.querySelectorAll('.app-classroom .sidenav')
    this.mSidenav = M.Sidenav.init(elems, {})[0]
  },
  beforeDestroy() {
    // HACK: typeerror this._overlay.parentNode is null
    console.log(this.mSidenav);
    Object.defineProperty(
      this.mSidenav._overlay,
      'parentNode', {
      value: document.body,
    })
    setTimeout(this.mSidenav.destroy(), 0)
  },
}