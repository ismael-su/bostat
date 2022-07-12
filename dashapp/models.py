
from datetime import datetime
from djongo import models

from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Distributeur(models.Model):
    _id = models.ObjectIdField()
    nom_distributeur = models.CharField(max_length=1000, blank=False)
    description_distributeur = models.TextField(blank=False)
    etat_distributeur = models.BooleanField(blank=False)
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())   
    
    def __str__(self) -> str:
        return self.nom_distributeur
    
class Societe(models.Model):
    _id = models.ObjectIdField()
    nom_societe = models.CharField(max_length=1000, blank=False)
    description_societe = models.TextField(blank=False)
    etat_societe = models.BooleanField(default=True)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    def __str__(self) -> str:
        return self.nom_societe
    
    
    
class Marque(models.Model):
    _id = models.ObjectIdField()
    nomarque = models.CharField(max_length=1000, blank=False)
    description_marque = models.TextField(blank=False)
    societeId = models.ForeignKey(Societe, db_column='societeId', on_delete=models.CASCADE)
    etat_marque = models.BooleanField(default=True)
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    def __str__(self) -> str:
        return self.nomarque
    
    



    
    
class Operation(models.Model):
    _id = models.ObjectIdField()
    libelle_operation = models.CharField(max_length=1000, blank=False)
    description_operation = models.TextField(blank=False)
    marqueId = models.ForeignKey(Marque, db_column='marqueId', on_delete=models.CASCADE)
    
    etat_operation = models.BooleanField(default=True)
    etat_fin_operation = models.BooleanField(default=True)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    def __str__(self) -> str:
        return self.libelle_operation
    
class Produit(models.Model):
    _id = models.ObjectIdField()
    titre_produit = models.CharField(max_length=1000, blank=False)
    description_produit = models.TextField(blank=False)
    
    etat_operation = models.BooleanField(default=True) # TODO
    url_redirection_produit = models.CharField(max_length=1000, blank=False)
    url_image_produit = models.CharField(max_length=1000, blank=False)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    operationId = models.ForeignKey(Operation, db_column='operationId', on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        return self.titre_produit

class Puce(models.Model):
    _id = models.ObjectIdField()
    numero_puce = models.CharField(max_length=1000, blank=False)
    libelle_puce = models.CharField(max_length=1000, blank=False)
    etat_puce = models.BooleanField(default=True)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    produitId = models.ForeignKey(Produit, db_column='produitId', on_delete=models.CASCADE)
    distributeurId = models.ForeignKey(Distributeur, db_column='distributeurId', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.libelle_puce


 


class Tamper(models.Model):
    _id = models.ObjectIdField()
    tamper = models.CharField(max_length=1000, blank=False)
    url_redirect_product = models.CharField(max_length=1000, blank=False)
    productId = models.ForeignKey(Produit, db_column='productId', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.tamper

class Customer(models.Model):
    _id = models.ObjectIdField()
    firstname = models.CharField(max_length=1000, blank=False)
    lastname = models.CharField(max_length=1000, blank=False)
    phone = models.CharField(max_length=1000, blank=False)
    email = models.CharField(max_length=250, blank=False,validators=[MinLengthValidator(4)] , unique=True)
    password = models.CharField(max_length=1000, blank=False, validators=[MinLengthValidator(8)])
    date = models.DateField(default=datetime.now())
    
    def save(self, *args, **kwargs):
        try:
            if not self.pk:
                user = User.objects.create(email=self.email, username=self.email, password=self.password)
                user.first_name=self.firstname
                user.last_name=self.lastname
                user.save()
            else:
                user = User.objects.get(email=self.email)
                user.first_name=self.firstname
                user.last_name=self.lastname
                user.save()
                
            super(Customer, self).save(*args, **kwargs)
        except:
            pass
    
    def delete(self):
        try:
            
            user = User.objects.get(email=self.email)
            user.delete()
            super(Customer, self).delete()
        except: pass
        
        
    
    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
 
 
class Question(models.Model):
    _id = models.ObjectIdField()
    jour = models.CharField(max_length=1000, blank=False)
    mois = models.CharField(max_length=1000, blank=False)
    annee = models.CharField(max_length=1000, blank=False)
    enfants = models.CharField(max_length=1000, blank=False)
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    produitId = models.ForeignKey(Produit, db_column='produitId', on_delete=models.CASCADE)
    puceId = models.ForeignKey(Puce, db_column='puceId', on_delete=models.CASCADE)
    userId = models.ForeignKey(Customer, db_column='userId', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.jour} {self.mois} {self.annee}"
    
    
      
    
class UserPro(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=1000, blank=False)
    email = models.CharField(max_length=1000, blank=False)
    
    def save(self, *args, **kwargs):
        try:
            if not self.pk:
                user: User
                user = User.objects.create(email=self.email, username=self.email, password=self.password)
                user.first_name=self.name
                user.is_staff
                #user.is_su
                user.save()
            else:
                user = User.objects.get(email=self.email)
                user.first_name=self.name
                user.save()
                
            super(UserPro, self).save(*args, **kwargs)
        except:
            pass
    
    def delete(self):
        try:
            
            user = User.objects.get(email=self.email)
            user.delete()
            super(UserPro, self).delete()
        except: pass
    
    def __str__(self) -> str:
        return f"{self.email}"
    
    
class CustomerAction(models.Model):
    _id = models.ObjectIdField()
    
    gps = models.CharField(max_length=1000, ) 
    systeme_exploitation = models.CharField(max_length=1000, )
    version_systeme = models.CharField(max_length=1000, )
    langue = models.CharField(max_length=1000, )
    tamper = models.CharField(max_length=1000, )
    custom_message = models.CharField(max_length=1000, )
    unique_code = models.CharField(max_length=1000, )
    
    date_creation = models.DateField(default=datetime.now())
    date_modification = models.DateField(default=datetime.now())
    
    idCustomer = models.ForeignKey(Customer, db_column='idCustomer', on_delete=models.CASCADE)
    idProduit = models.ForeignKey(Produit, db_column='idProduit', on_delete=models.CASCADE)
    idPuce = models.ForeignKey(Puce,db_column='idPuce', on_delete=models.CASCADE)
    idDistributeur = models.ForeignKey(Distributeur, db_column='idDistributeur', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.tamper} {self.idCustomer}"
    