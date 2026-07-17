from django.db import models

# Create your models here.
class Auteur(models.Model):
    nom=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)

    def __str__(self):
        return f"Auteur: {self.nom}"
    
class Article(models.Model): 
    titre= models.CharField( max_length=50)         
    description=models.TextField()
    image=models.ImageField(upload_to="blogs/",null=True)
    date_creation=models.DateField( auto_now=True)
    auteur=models.ForeignKey('Auteur' ,on_delete=models.CASCADE)
     
    def __str__(self):
        return f"{self.titre}"
    class Meta:
        ordering = ['-date_creation']   
         