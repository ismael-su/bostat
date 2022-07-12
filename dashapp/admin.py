from django.contrib import admin
import bson
from .models import (
    Societe, Operation, Marque,
    Puce, Customer, CustomerAction,
    UserPro, Question, Tamper,
    Produit, Distributeur
)

class SocieteAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Societe._meta.fields if not f.name in ['_id']]

class OperationAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Operation._meta.fields if not f.name in ['_id', 'marqueId']]
    
    def get_form(self, request, obj, **kwargs):
        if request.POST:
            # remember old state
            _mutable = request.POST._mutable
            # set to mutable
            request.POST._mutable = True
            # Change the values you want
            request.POST['marqueId'] = bson.ObjectId(request.POST['marqueId'])
            # set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, **kwargs)

class MarqueAdmin(admin.ModelAdmin):
    
    list_display  = [f.name for f in Marque._meta.fields if not f.name in ['_id', 'societeId']]
    
    
    def get_form(self, request, obj, **kwargs):
        if request.POST:
            # remember old state
            _mutable = request.POST._mutable
            # set to mutable
            request.POST._mutable = True
            # Change the values you want
            request.POST['societeId'] = bson.ObjectId(request.POST['societeId'])
            # set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, **kwargs)
    #exclude = ('societeId',)

class PuceAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Puce._meta.fields if not f.name in ['_id']]
    
    def get_form(self, request, obj, **kwargs):
        if request.POST:
            # remember old state
            _mutable = request.POST._mutable
            # set to mutable
            request.POST._mutable = True
            # Change the values you want
            request.POST['produitId'] = bson.ObjectId(request.POST['produitId'])
            request.POST['distributeurId'] = bson.ObjectId(request.POST['distributeurId'])
            # set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, **kwargs)

class CustomerAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Customer._meta.fields if not f.name in ['_id']]

class CustomerActionAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in CustomerAction._meta.fields if not 'id' in f.name]
    def get_form(self, request, obj, **kwargs):
        if request.POST:
            # remember old state
            _mutable = request.POST._mutable
            # set to mutable
            request.POST._mutable = True
            # Change the values you want
            request.POST['idProduit'] = bson.ObjectId(request.POST['idProduit'])
            request.POST['idPuce'] = bson.ObjectId(request.POST['idPuce'])
            request.POST['idDistributeur'] = bson.ObjectId(request.POST['idDistributeur'])
            request.POST['idCustomer'] = bson.ObjectId(request.POST['idCustomer'])
            # set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, **kwargs)

class UserProAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in UserPro._meta.fields if not f.name in ['_id']]

class QuestionAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Question._meta.fields if not ('id' in  f.name  or 'Id' in f.name)]
    def get_form(self, request, obj, **kwargs):
        if request.POST:
            # remember old state
            _mutable = request.POST._mutable
            # set to mutable
            request.POST._mutable = True
            # Change the values you want
            request.POST['produitId'] = bson.ObjectId(request.POST['produitId'])
            request.POST['puceId'] = bson.ObjectId(request.POST['puceId'])
            request.POST['userId'] = bson.ObjectId(request.POST['userId'])
            # set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, **kwargs)

class TamperAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Tamper._meta.fields if not ('id' in  f.name  or 'Id' in f.name)]
    
    def get_form(self, request, obj, **kwargs):
        if request.POST:
            # remember old state
            _mutable = request.POST._mutable
            # set to mutable
            request.POST._mutable = True
            # Change the values you want
            request.POST['productId'] = bson.ObjectId(request.POST['productId'])
            # set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, **kwargs)

class ProduitAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Produit._meta.fields if not ('id' in  f.name  or 'Id' in f.name)]
    
    def get_form(self, request, obj, **kwargs):
        if request.POST:
            # remember old state
            _mutable = request.POST._mutable
            # set to mutable
            request.POST._mutable = True
            # Change the values you want
            request.POST['operationId'] = bson.ObjectId(request.POST['operationId'])
            # set mutable flag back
            request.POST._mutable = _mutable

        return super().get_form(request, obj=obj, **kwargs)

class DistributeurAdmin(admin.ModelAdmin):
    list_display  = [f.name for f in Distributeur._meta.fields if not f.name in ['_id']]





admin.site.register(Societe, SocieteAdmin)
admin.site.register(Distributeur, DistributeurAdmin)
admin.site.register(Produit, ProduitAdmin)
admin.site.register(Tamper, TamperAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserPro, UserProAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAction, CustomerActionAdmin)
admin.site.register(Puce, PuceAdmin)
admin.site.register(Marque, MarqueAdmin)
admin.site.register(Operation, OperationAdmin)
