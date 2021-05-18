// User defined strings
import en from './en'
import uz from './uz'

export const strings = {en, uz}
export const availableLocales = ['en', 'uz']
export const defaultLocale = 'en'
console.assert(availableLocales.includes(defaultLocale))

export let locale = function() {
  const lang = localStorage.getItem('language')
  if (lang)
    if (availableLocales.includes(lang)) {
      return lang
    }
    else {
      localStorage.setItem('language', defaultLocale)
      return defaultLocale
    }
  else
    return availableLocales.find(i => i.startsWith(navigator.language)) || defaultLocale
}()


/**
 * @param {String} name
 * @param {Object} args
 * @param {Object} strings
 * @returns {String}
 */
export function t(name, args, strings = strings) {
  /** @type {String} */
  let message = strings[locale][name]
  if (message && args) return message
  if (!message) message = strings[defaultLocale]
  if (!message) console.warn('[STRINGS] Error: key "'+name+'"Doesn\'t exist')
  return message.replaceAll(/{([a-zA-Z0-9])}/g, (a, key) => {
    return args[key]
  })
}

export default { install(Vue) {
  Vue.mixin({
    methods: {
      /**
       * @param {String} name
       * @param {Object} args
       * @returns {String}
       */
      $t(name, args) {
        if (this.$options)
          return t(name, args, this.$options) || t(name, args)
        return t(name, args)
      }
    }
  })
}}
