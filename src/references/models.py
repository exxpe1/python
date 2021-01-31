from django.db import models

# Create your models here.

class Author(models.Model):
    
    name_author = models.CharField(
        verbose_name ='Автор',
        max_length=50
        )
    desc_author = models.TextField(
        verbose_name ='Краткая информация об авторе',
        max_length=50,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.name_author

class Series(models.Model):
    name_series = models.CharField(
        verbose_name ='Серия',
        max_length=50
        )

    def __str__(self):
        return self.name_series

class Publisher(models.Model):
    name_publisher = models.CharField(
        verbose_name ='Издатель',
        max_length=50
        )

    def __str__(self):
        return self.name_publisher

class Genre(models.Model):
    name_genre = models.CharField(
        verbose_name ='Жанр',
        max_length=50
        )

    def __str__(self):
        return self.name_genre