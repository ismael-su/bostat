const { Schema, model } = require('mongoose')

const Question = model('Question', {
  jour: {
    type: String,
    required: true,
  },
  mois: {
    type: String,
    required: true,
  },
  annee:{
    type: String,
    default: true
  },
  enfants: {
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
  produitId: {
    type: Schema.Types.ObjectId,
    ref: 'Produit',
  },
  puceId: {
    type: Schema.Types.ObjectId,
    ref: 'Puce',
  },
  userId: {
    type: Schema.Types.ObjectId,
    ref: 'Customer',
  },
})

module.exports = Question
