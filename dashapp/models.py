
from datetime import datetime
from djongo import models
 

class Distributeur(models.Model):
    _id = models.ObjectIdField()
    nom_distributeur = models.TextField(blank=False)
    description_distributeur = models.TextField(blank=False)
    etat_distributeur = models.BooleanField(blank=False)
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())   
    
class Societe(models.Model):
    _id = models.ObjectIdField()
    nom_societe = models.TextField(blank=False)
    description_societe = models.TextField(blank=False)
    etat_societe = models.BooleanField(default=True)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
class Marque(models.Model):
    _id = models.ObjectIdField()
    nomarque = models.TextField(blank=False)
    description_marque = models.TextField(blank=False)
    societeId = models.EmbeddedField(model_container=Societe)
    etat_marque = models.BooleanField(default=True)
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())

    
    
class Operation(models.Model):
    _id = models.ObjectIdField()
    libelle_operation = models.TextField(blank=False)
    description_operation = models.TextField(blank=False)
    marqueId = models.EmbeddedField(model_container=Marque)
    
    etat_operation = models.BooleanField(default=True)
    etat_fin_operation = models.BooleanField(default=True)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
class Produit(models.Model):
    _id = models.ObjectIdField()
    titre_produit = models.TextField(blank=False)
    description_produit = models.TextField(blank=False)
    
    etat_operation = models.BooleanField(default=True) # TODO
    url_redirection_produit = models.TextField(blank=False)
    url_image_produit = models.TextField(blank=False)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    operationId = models.EmbeddedField(model_container=Operation)

class Puce(models.Model):
    _id = models.ObjectIdField()
    numero_puce = models.TextField(blank=False)
    libelle_puce = models.TextField(blank=False)
    etat_puce = models.BooleanField(default=True)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    produitId = models.EmbeddedField(model_container=Produit)
    distributeurId = models.EmbeddedField(model_container=Distributeur)


 


class Tamper(models.Model):
    _id = models.ObjectIdField()
    tamper = models.TextField(blank=False)
    url_redirect_product = models.TextField(blank=False)
    productId = models.EmbeddedField(model_container=Produit)

class Customer(models.Model):
    _id = models.ObjectIdField()
    firstname = models.TextField(blank=False)
    lastname = models.TextField(blank=False)
    phone = models.TextField(blank=False)
    email = models.TextField(blank=False)
    password = models.TextField(blank=False)
    date = models.DateField(default=datetime.now())
 
 
class Question(models.Model):
    _id = models.ObjectIdField()
    jour = models.TextField(blank=False)
    mois = models.TextField(blank=False)
    annee = models.TextField(blank=False)
    enfants = models.TextField(blank=False)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    produitId = models.EmbeddedField(model_container=Produit)
    puceId = models.EmbeddedField(model_container=Puce)
    userId = models.EmbeddedField(model_container=Customer)
      
    
class UserPro(models.Model):
    _id = models.ObjectIdField()
    name = models.TextField(blank=False)
    email = models.TextField(blank=False)
    
    
class CustomerAction(models.Model):
    _id = models.ObjectIdField()
    
    gps = models.TextField() 
    systeme_exploitation = models.TextField()
    version_systeme = models.TextField()
    langue = models.TextField()
    tamper = models.TextField()
    custom_message = models.TextField()
    unique_code = models.TextField()
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    idCustomer = models.EmbeddedField(model_container=Customer)
    idProduit = models.EmbeddedField(model_container=Produit)
    idPuce = models.EmbeddedField(model_container=Puce)
    idDistributeur = models.EmbeddedField(model_container=Distributeur)
    