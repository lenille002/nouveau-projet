from django.db import models

# Create your models here.
class produit(models.Model):
    designation=models.CharField(max_length=100)
    categorie=models.CharField(max_length=50)
    prix_achat=models.DecimalField(max_digits=10,decimal_places=2)
    prix_vente=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    date_creation=models.DateField(auto_now_add=True)

    def benefice(self):
        return self.prix_vente - self.prix_achat
    
    def __str__(self):
        return self.designation
#commande
class commande(models.Model):
    statut=[("en attente","en attente"),("validée","validée"),("livrée","livrée"),] 
    numero_commande=models.CharField(max_length=30)
    fournisseur=models.CharField(max_length=100)
    date_commande=models.DateField()
    statut=models.CharField(max_length=20,choices=statut)
    produits=models.ManyToManyField(produit)

    def __str__(self):
        return self.numero_commande
#livraison
class livraison(models.Model):
    numero_livraison=models.CharField(max_length=30)
    date_livraison=models.DateField()
    observation=models.TextField()
    produit=models.ManyToManyField(produit)

    def __str__(self):
        return self.numero_livraison
    
#vente
class vente(models.Model):
    numero_vente=models.CharField(max_length=30)
    date_vente=models.DateField()
    nom_client=models.CharField(max_length=100)
    mode_paiement=models.CharField(max_length=50)
    produits=models.ManyToManyField(produit)

    def __str__(self):
        return self.numero_vente


    

