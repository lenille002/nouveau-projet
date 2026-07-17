from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .models import Article


def accueil(request):
    articles = Article.objects.all().order_by("-date_creation")[:3]
    return render(request, "blog/accueil.html", {"articles": articles})


def blog(request):
    articles = Article.objects.all().order_by("-date_creation")
    return render(request, "blog/blog.html", {"articles": articles})


def contact(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        sujet = request.POST.get("sujet")
        message = request.POST.get("message")

        contenu = f"""
Nom : {nom}
Email : {email}

Message :
{message}
"""

        try:
            send_mail(
                subject=sujet,
                message=contenu,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            return render(
                request,
                "blog/contact.html",
                {
                    "success": "Votre message a été envoyé avec succès."
                },
            )

        except Exception as e:
            return render(
                request,
                "blog/contact.html",
                {
                    "error": f"Erreur lors de l'envoi : {e}"
                },
            )

    return render(request, "blog/contact.html")