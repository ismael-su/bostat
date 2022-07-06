const { Schema, model } = require('mongoose')

const Societe = model('Societe', {
  nom_societe: {
    type: String,
    required: true,
  },
  description_societe:{
    type: String,
    required: true
  },
  etat_societe:{
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

module.exports = Societe
