# Generated by Django 3.1.5 on 2021-02-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0005_auto_20210203_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='genre',
            field=models.ManyToManyField(to='references.Genre', verbose_name='Жанр'),
        ),
    ]
