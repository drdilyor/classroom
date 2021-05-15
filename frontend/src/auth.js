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
    if (jwt)
      auth.payload = auth.decodeJwt(jwt)
    this.inited = true
  },

  decodeJwt(token) {
    var base64Url = token.split('.')[1]
    var base64 = decodeURIComponent(atob(base64Url).split('').map(
      c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
    ).join(''))
    var result = JSON.parse(base64)

    return result
  },

  setJwt(jwt) {
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
    window.location = `https://${auth.config.domain}/authorize?audience=${auth.config.audience}&response_type=token&scope=openid profile email&client_id=${auth.config.clientId}&redirect_uri=${callbackUrl}`
  },
  
  logout() {
    localStorage.removeItem('jwt')
    auth.payload = null
  },

  logoutHard() {
    window.location = `https://${auth.config.domain}/logout`
  },

  can(perm) {
    return auth.payload.permissions.includes(perm)
  },
  
  getProfile() {
    console.assert(this.loggedIn())
    return new Promise((resolve, reject) => {
      fetch(`https://${auth.config.domain}/userinfo`, {
        headers: {authorization: `Bearer ${auth.getJwt()}`}
      })
      .then(res => {
        if (res.status !== 200) auth.login()
        else return res.json()
      })
      .then(data => {
        console.log(data)
        resolve(data)
      })
      .catch(err => {
        reject(err)
      })
    })
  }
}

module.exports = auth
