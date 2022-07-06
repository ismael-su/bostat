const { Schema, model } = require('mongoose')

const CustomerAction = model('CustomerAction', {
  gps: {
    type: String,
  },
  systeme_exploitation: {
    type: String,
  },
  version_systeme:{
    type: String,
  },
  langue: {
    type: String,
  },
  tamper:{
      type: String
  },
  custom_message:{
    type: String
  },
  unique_code:{
    type: String
  },
  date_creation:{
    type: Date,
    default: Date.now()
  },
  date_modification:{
    type: Date,
    default: Date.now()
  },
  idCustomer: {
    type: Schema.Types.ObjectId,
    ref: 'Customer',
  },
  idProduit: {
    type: Schema.Types.ObjectId,
    ref: 'Produit',
  },
  idPuce: {
    type: Schema.Types.ObjectId,
    ref: 'Puce',
  },
  idDistributeur: {
    type: Schema.Types.ObjectId,
    ref: 'Distributeur',
  },

})

module.exports = CustomerAction
