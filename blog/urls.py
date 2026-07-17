from django.urls import path 
from . import views

urlpatterns = [

    path('accueil/', views.accueil,name='accueil'),
    path('contact/', views.contact,name='contact'),
    path('blog/', views.blog,name='blog'),
    
]


