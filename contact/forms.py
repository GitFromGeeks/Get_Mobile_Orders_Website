from django.core import validators
from django import forms
from .models import contactModel

class contactform(forms.ModelForm):
 class Meta:
  model = contactModel
  fields = ['name', 'phone','message']

