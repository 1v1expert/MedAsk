# Generated by Django 2.1.5 on 2019-10-27 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancedata',
            name='format_number',
            field=models.CharField(default=None, max_length=255, verbose_name='Формат СП'),
        ),
    ]
