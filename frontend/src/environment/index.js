module.exports = process.env.NODE_ENV === 'production'
  ? require('./environment.prod.js')
  : require('./environment.dev.js')
