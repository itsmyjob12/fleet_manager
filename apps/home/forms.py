from django import forms
from .models import Chauffeur

class ChauffeurForm(forms.ModelForm):
    class Meta:
        model = Chauffeur
        fields = ['nom', 'prenom', 'email', 'telephone', 'adresse']
