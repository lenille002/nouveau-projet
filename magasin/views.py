from django.http import HttpResponse

def accueil(request):
    return HttpResponse("bienvenue dans l'application Magasin")

# Create your views here.
