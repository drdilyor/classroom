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
 * @param {*} defaultValue
 * @param {Object} stringz
 * @returns {String}
 */
export function t(name, args = null, defaultValue = null, stringz = strings) {
  // optimize the simplest case
  /** @type {String} */
  let message = stringz[locale] && stringz[locale][name]
  if (message && !args) return message

  let _
  // fallback locale
  if (!message
    && locale !== defaultLocale
    && (_ = stringz[defaultLocale])
    && (_ = _[name]))
      message = _
  // in case nothing was found
  if (!message) {
    if (defaultValue === null) {
      console.warn('[STRINGS] Error: key "' + name + '" doesn\'t exist')
      return ''
    }
    else {
      message = defaultValue
    }
  }

  if (message && !args) return message

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
      $t(name, args = null) {
        if (this.$options.strings)
          return t(name, args, '', this.$options.strings) || t(name, args)
        return t(name, args)
      }
    }
  })
}}
