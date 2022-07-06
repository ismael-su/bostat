const { Schema, model } = require('mongoose')

const Puce = model('Puce', {
  numero_puce: {
    type: String,
    required: true,
  },
  libelle_puce: {
    type: String,
    required: true,
  },
  etat_puce:{
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
  },
  produitId: {
    type: Schema.Types.ObjectId,
    ref: 'Produit',
  },
  distributeurId: {
    type: Schema.Types.ObjectId,
    ref: 'Distributeur',
  },
})

module.exports = Puce
