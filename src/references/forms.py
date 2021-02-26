from django import forms
from django.db.models import fields
from . import models

class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ('name_product','price')

class AuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = ('name_author','desc_author')

class GenreForm(forms.ModelForm):

    class Meta:
        model = models.Genre
        fields = ('name_genre','desc_genre')

class PublisherForm(forms.ModelForm):

    class Meta:
        model = models.Publisher
        fields = ('name_publisher','desc_publisher')

class SeriesForm(forms.ModelForm):

    class Meta:
        model = models.Series
        fields = ('name_series','desc_series')