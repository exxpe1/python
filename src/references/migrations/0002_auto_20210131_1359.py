# Generated by Django 3.1.5 on 2021-01-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_series', models.CharField(max_length=50, verbose_name='Серия')),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='desc_author',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Краткая информация об авторе'),
        ),
    ]
