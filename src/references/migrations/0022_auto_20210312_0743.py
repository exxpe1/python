# Generated by Django 3.1.5 on 2021-03-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0021_auto_20210312_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='ISBN'),
        ),
    ]
