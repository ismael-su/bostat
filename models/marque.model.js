const { Schema, model } = require('mongoose')

const Marque = model('Marque', {
  nomarque: {
    type: String,
    required: true,
  },
  description_marque: {
    type: String,
    required: true,
  },
  societeId: {
    type: Schema.Types.ObjectId,
    ref: 'Societe',
  },
  etat_marque:{
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

module.exports = Marque
