const { Schema, model } = require('mongoose')

const Tamper = model('Tamper', {
  tamper: {
    type: String,
    required: true,
  },
  url_redirect_product: {
    type: String,
    required: true,
  },
  productId: {
    type: Schema.Types.ObjectId,
    ref: 'Produit',
  },
})

module.exports = Tamper
