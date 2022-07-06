const { Schema, model } = require('mongoose')

const Distributeur = model('Distributeur', {
  nom_distributeur: {
    type: String,
    required: true,
  },
  description_distributeur: {
    type: String,
    required: true,
  },
  etat_distributeur:{
    type: Boolean,
    default: true
  },
  date_creation:{
    type: Date,
    default: Date.now()
  },
  date_modification:{
    type: Date,
    default: Date.now()
  }
})

module.exports = Distributeur
