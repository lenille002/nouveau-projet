from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'})
    )
    sujet = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sujet'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Votre message'})
    )