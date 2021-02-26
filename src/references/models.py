from django.db import models


# Create your models here.

class Author(models.Model):
    
    name_author = models.CharField(
        verbose_name ='Автор',
        max_length=50)
    desc_author = models.TextField(
        verbose_name ='Краткая информация об авторе',
        max_length=50,
        null=True,
        blank=True)

    def __str__(self):
        return self.name_author
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'



class Series(models.Model):
    name_series = models.CharField(
        verbose_name ='Серия',
        max_length=50)

    desc_series = models.TextField(
        verbose_name ='Краткая информация о серии',
        max_length=50,
        null=True,
        blank=True)

    def __str__(self):
        return self.name_series

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

class Publisher(models.Model):
    name_publisher = models.CharField(
        verbose_name ='Издатель',
        max_length=50)

    desc_publisher = models.TextField(
        verbose_name ='Краткая информация об Издателе',
        max_length=50,
        null=True,
        blank=True)

    def __str__(self):
        return self.name_publisher
    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
class Genre(models.Model):
    name_genre = models.CharField(
        verbose_name ='Жанр',
        max_length=50)
    desc_genre = models.TextField(
        verbose_name ='Краткая информация о Жанре',
        max_length=50,
        null=True,
        blank=True)
    def __str__(self):
        return self.name_genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Product(models.Model):
    name_product = models.CharField(
        verbose_name ='Название книги',
        max_length=80)
    author = models.ManyToManyField(
        'Author',
        verbose_name ='Автор')
    serie = models.ForeignKey(
        'Series',
        verbose_name ='Серия',
        on_delete=models.PROTECT,
        blank=True,
        null=True)
    genre = models.ManyToManyField(
        'Genre',
        verbose_name ='Жанр'
    )
    year = models.CharField(
        verbose_name ='Год издания'
        ,max_length=50,
        blank=True,
        null=True)
    pages = models.IntegerField(
        verbose_name ='Страниц',
        blank=True,
        null=True)
    cover = models.CharField(
        verbose_name ='Переплет',
        max_length=50,
        blank=True,
        null=True)
    format = models.CharField(
        verbose_name ='Формат',
        max_length=50,
        blank=True,
        null=True)
    isbn = models.IntegerField(
        verbose_name ='ISBN',
        blank=True,
        null=True)  
    weight = models.IntegerField(
        verbose_name='Вес(гр)',
        blank=True,
        null=True)
    age_restrict = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length=50,
        null=True)
    publisher = models.ForeignKey(
        'Publisher',
        verbose_name ='Издатель',
        on_delete=models.PROTECT,
        blank=True,
        null=True)
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name ='Цена',
        null=True)
    created = models.DateTimeField(
        verbose_name ='Создано',
        auto_now=False,
        null=True)
    updated = models.DateTimeField(
        verbose_name ='Обновлено',
        auto_now=True,
        null=True)
    image = models.ImageField(
        null=True,
        blank = True,
        upload_to = 'image/'
    )
    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'