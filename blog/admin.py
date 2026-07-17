from django.contrib import admin
from .models import Auteur, Article

# Register your models here.
@admin.register(Auteur)
class Auteuradmin(admin.ModelAdmin):
    list_display=("nom","email",)
    search_fields=("nom",) #barre de recherche
    list_filter=("nom",)
@admin.register(Article)
class Articleadmin(admin.ModelAdmin):
    list_display=("titre",'description','auteur','date_creation','image',)#barre de recherche
    list_filter=("titre",)    
