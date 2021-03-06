# Generated by Django 2.1.5 on 2019-10-27 23:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Страховая компания',
                'verbose_name_plural': 'Страховые компании',
            },
        ),
        migrations.CreateModel(
            name='InsuranceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Когда создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Когда обновлено')),
                ('is_public', models.BooleanField(default=True, verbose_name='Опубликовано?')),
                ('deleted', models.BooleanField(default=False, editable=False, verbose_name='В архиве?')),
                ('policy_number', models.CharField(max_length=255, verbose_name='Номер СП')),
                ('type_of_insurance', models.CharField(choices=[('oms', 'ОМС'), ('dms', 'ДМС')], max_length=4, verbose_name='Тип страхования')),
                ('expiration_date', models.DateField(verbose_name='Дата окончания')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.InsuranceCompany')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем создано')),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Кем обновлено')),
            ],
            options={
                'verbose_name': 'Базовая модель ',
                'verbose_name_plural': 'Базовые модели',
                'abstract': False,
            },
        ),
    ]
