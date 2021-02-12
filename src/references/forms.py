from django import forms
from django.db.models import fields
from . import models

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ('name_product','price')