from django.contrib import admin

from .models import (
    Societe, Operation, Marque,
    Puce, Customer, CustomerAction,
    UserPro, Question, Tamper,
    Produit, Distributeur
)

class SocieteAdmin(admin.ModelAdmin):
    pass

class OperationAdmin(admin.ModelAdmin):
    pass

class MarqueAdmin(admin.ModelAdmin):
    pass

class PuceAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass

class CustomerActionAdmin(admin.ModelAdmin):
    pass

class UserProAdmin(admin.ModelAdmin):
    pass

class QuestionAdmin(admin.ModelAdmin):
    pass

class TamperAdmin(admin.ModelAdmin):
    pass

class ProduitAdmin(admin.ModelAdmin):
    pass

class DistributeurAdmin(admin.ModelAdmin):
    pass





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
