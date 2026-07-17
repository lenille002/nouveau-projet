from django.contrib import admin
from .models import produit,commande,livraison,vente
# Register your models here.
@admin.register(produit)
class produitadmin(admin.ModelAdmin):
    list_display=("designation","categorie","prix_achat","prix_vente","benefice","date_creation",)
    search_fields=("designation","categorie",)
    list_filter=("categorie",)
    ordering=("designation",)
    
@admin.register(commande)
class commandeadmin(admin.ModelAdmin):
    list_display=("numero_commande","fournisseur","date_commande","statut",)
    search_fields=("numero_commande","fournisseur",)
    list_filter=("statut","date_commande",)
    ordering=("numero_commande",)

@admin.register(livraison)
class livraisonadmin(admin.ModelAdmin):
    list_display=("numero_livraison","date_livraison","observation",)
    search_fields=("numero_livraison",)
    list_filter=('date_livraison',)
    ordering=("numero_livraison",)

@admin.register(vente)
class venteadmin(admin.ModelAdmin):
    list_display=("numero_vente","nom_client","date_vente","mode_paiement",)
    search_fields=("numero_vente","nom_client",)
    list_filter=("mode_paiement","date_vente",)
    ordering=("numero_vente",)    
        

