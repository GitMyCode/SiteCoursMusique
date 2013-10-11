
from django.forms import ModelForm,Form, TextInput, forms
from django.forms import IntegerField, CharField, DecimalField
from django.models import (
                           Professeurs,
                           Cours,
                           Gallerie,
                           )

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
