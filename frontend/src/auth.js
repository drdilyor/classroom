const auth = {
  config: {
    domain: 'drdilyor.us.auth0.com',
    clientId: 'MkEkDPWlI5UeoA4wIOtqcCBGkquaAy3t',
    audience: 'classroomapi',
    
  },
  registerRouter(r) {
    r.beforeEach((to, from, next) => {
      if (to.matched.some(record => record.meta.requiresAuth)) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        if (!auth.loggedIn()) {
          auth.login()
        } else {
          next()
        }
      } else {
        next() // make sure to always call next()!
      }
    })
    return r
  },

  payload: null,
  inited: false,

  init() {
    const jwt = localStorage.getItem('jwt')
    console.log('init');
    console.log({jwt});
    if (jwt) {
      auth.payload = auth.decodeJwt(jwt)
      console.log({payload: auth.payload});
    }
    this.inited = true
  },

  decodeJwt(token) {
    var base64Url = token.split('.')[1]
    var base64 = decodeURIComponent(atob(base64Url).split('').map(
      c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
    ).join(''))
    var result = JSON.parse(base64)

    console.log('decoded jwt')
    console.log({result, token})

    return result
  },

  setJwt(jwt) {
    console.log('set jwt');
    console.log({jwt});
    try {
      auth.payload = auth.decodeJwt(jwt)
    } catch {
      console.log('failed to decode ' + jwt);
      return false
    }
    localStorage.setItem('jwt', jwt)
    return true
  },

  getJwt() {
    return localStorage.getItem('jwt')
  },

  loggedIn() {
    if (!this.inited) this.init()
    return this.payload != null
  },

  login() {
    let callbackUrl = `https://${location.host}/profile`
    window.location = `https://${auth.config.domain}/authorize?audience=${auth.config.audience}&response_type=token&client_id=${auth.config.clientId}&redirect_uri=${callbackUrl}`
  },
  
  logout() {
    localStorage.removeItem('jwt')
    auth.payload = null
  },

  can(perm) {
    return auth.payload.permissions.includes(perm)
  }
}

module.exports = auth
