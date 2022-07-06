const { Schema, model } = require('mongoose')

const Produit = model('Produit', {
  titre_produit: {
    type: String,
    required: true,
  },
  description_produit: {
    type: String,
    required: true,
  },
  etat_operation:{
    type: Boolean,
    default: true
  },
  url_redirection_produit: {
    type: String,
    required: true,
  },
  url_image_produit: {
    type: String,
    required: true,
  },
  date_creation:{
    type: Date,
    default: Date.now()
  },
  date_modification:{
    type: Date,
    default: Date.now()
  },
  operationId: {
    type: Schema.Types.ObjectId,
    ref: 'Operation',
  },
})

module.exports = Produit
