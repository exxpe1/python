# Generated by Django 3.1.5 on 2021-02-04 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0010_auto_20210204_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]
