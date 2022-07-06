const { model } = require('mongoose')

const User = model('UserPro', {
  name: String,
  email: String,
})

module.exports = User
