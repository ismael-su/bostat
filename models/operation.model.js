const { Schema, model } = require('mongoose')

const Operation = model('Operation', {
  libelle_operation: {
    type: String,
    required: true,
  },
  description_operation: {
    type: String,
    required: true,
  },
  marqueId: {
    type: Schema.Types.ObjectId,
    ref: 'Marque',
  },
  etat_operation:{
    type: Boolean,
    default: true
  },
  date_fin_operation:{
    type: Date,
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

module.exports = Operation
