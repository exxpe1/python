from django.contrib import admin
from . import models
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name_author']
    list_display = [
        'pk',
        'name_author',
        'desc_author'
    ]


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Series)
admin.site.register(models.Publisher)
admin.site.register(models.Genre)
admin.site.register(models.Product)