# Generated by Django 3.1.5 on 2021-02-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0013_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
