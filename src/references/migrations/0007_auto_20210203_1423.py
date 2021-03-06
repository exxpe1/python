# Generated by Django 3.1.5 on 2021-02-03 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0006_product_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='references.publisher', verbose_name='Издатель'),
        ),
        migrations.AddField(
            model_name='product',
            name='serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='references.series', verbose_name='Серия'),
        ),
    ]
