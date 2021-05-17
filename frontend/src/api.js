import auth from '@/auth'
import {SnackbarProgrammatic as snackbar} from "buefy";

function required() {
  throw TypeError()
}

const api = {
  backend: require('@/environment').backend,
  get(...args) {
    return api.request('GET', ...args)
  },
  async request(method=required(), endpoint=required(), body, options) {
    console.log('api request')

    if (endpoint.startsWith('/'))
      endpoint = endpoint.slice(1)

    const fetchArgs = {method, headers: {}}
    if (body) {
      fetchArgs.body = JSON.stringify(body)
      fetchArgs.headers['Content-Type'] = 'application/json'
    }
    if (auth.loggedIn())
      fetchArgs.headers.Authorization = `Bearer ${auth.getJwt()}`
    //console.log({fetchArgs})
    try {
      const res = await fetch(`${api.backend}/${endpoint}`, Object.assign(fetchArgs, options))
      switch(res.status) {
        case 200:
          //console.log('ok')
          break
        case 401:
          // Error with JWT, obtain a new one
          snackbar.open('Error: token expired. Refreshing. Please wait...')
          auth.login()
          break
      }
      return res.json()
    }
    catch (e) {
      console.error(e)
      throw e
    }
  },
}

export default api;

