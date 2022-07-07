
from dataclasses import field
from datetime import datetime
from mongoengine import Document, fields
from pkg_resources import require



       
class CustomerAction(Document):
    
    gps = fields.StringField() 
    systeme_exploitation = fields.StringField()
    version_systeme = fields.StringField()
    langue = fields.StringField()
    tamper = fields.StringField()
    custom_message = fields.StringField()
    unique_code = fields.StringField()
    
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())
    
    idCustomer = fields.ReferenceField('Customer')
    idProduit = fields.ReferenceField('Produit')
    idPuce = fields.ReferenceField('Puce')
    idDistributeur = fields.ReferenceField('Distributeur')
    
class Distributeur(Document):
    
    nom_distributeur = fields.StringField(required=True)
    description_distributeur = fields.StringField(required=True)
    etat_distributeur = fields.BooleanField(required=True)
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())   
    
class Marque(Document):
    
    nomarque = fields.StringField(required=True)
    description_marque = fields.StringField(required=True)
    societeId = fields.ReferenceField('Societe')
    etat_marque = fields.BooleanField(default=True)
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())
    
    
class Operation(Document):
    
    libelle_operation = fields.StringField(required=True)
    description_operation = fields.StringField(required=True)
    marqueId = fields.ReferenceField('Marque')
    
    etat_operation = fields.BooleanField(default=True)
    etat_fin_operation = fields.BooleanField(default=True)
    
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())
    
class Produit(Document):
    
    titre_produit = fields.StringField(required=True)
    description_produit = fields.StringField(required=True)
    
    etat_operation = fields.BooleanField(default=True) # TODO
    url_redirection_produit = fields.StringField(required=True)
    url_image_produit = fields.StringField(required=True)
    
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())
    operationId = fields.ReferenceField('Operation')

class Puce(Document):
    
    numero_puce = fields.StringField(required=True)
    libelle_puce = fields.StringField(required=True)
    etat_puce = fields.BooleanField(default=True)
    
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())
    
    produitId = fields.ReferenceField('Produit')
    distributeurId = fields.ReferenceField('Distributeur')


class Question(Document):
    jour = fields.StringField(required=True)
    mois = fields.StringField(required=True)
    annee = fields.StringField(required=True)
    enfants = fields.StringField(required=True)
    
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())
    
    produitId = fields.ReferenceField('Produit')
    puceId = fields.ReferenceField('Puce')
    userId = fields.ReferenceField('Customer')
    

class Societe(Document):
    nom_societe = fields.StringField(required=True)
    description_societe = fields.StringField(required=True)
    etat_societe = fields.BooleanField(default=True)
    
    date_creation = fields.DateField(default=datetime.now())
    date_modification = fields.DateField(default=datetime.now())
    

class Tamper(Document):
    
    tamper = fields.StringField(required=True)
    url_redirect_product = fields.StringField(required=True)
    productId = fields.ReferenceField('Produit')

class Customer(Document):
    
    firstname = fields.StringField(required=True)
    lastname = fields.StringField(required=True)
    phone = fields.StringField(required=True)
    email = fields.StringField(required=True)
    password = fields.StringField(required=True)
    date = fields.DateField(default=datetime.now())
    
    
class UserPro(Document):
    name = fields.StringField(required=True)
    email = fields.StringField(required=True)
    
    
  
  