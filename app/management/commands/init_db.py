from django.core.management.base import BaseCommand
from app.models import InsuranceData, InsuranceCompany
from app.choices import OMS, DMS
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

companies = [
    {
        'title': 'СК МЕД-АСКЕР',
        'phone': '8 (495) 123-45-67'
    },
    {
        'title': 'СК Рандеву',
        'phone': '8 (499) 123-45-68'
    },
    {
        'title': 'Страх-трах',
        'phone': '8 (812) 123-45-69'
    },
]

company_data = [
    {
        'policy_number': '1234 12345678',
        'format_number': '1111011111111',
        'type_of_insurance': DMS,
        'expiration_date': '14.08.2020',
        'company': 'СК МЕД-АСКЕР'
    },
    {
        'policy_number': '9876 543210',
        'format_number': '11110111111',
        'type_of_insurance': OMS,
        'expiration_date': '15.08.2021',
        'company': 'СК МЕД-АСКЕР'
    },
    {
        'policy_number': '1234-123456-78',
        'format_number': '11110111111011',
        'type_of_insurance': DMS,
        'expiration_date': '16.08.2022',
        'company': 'СК Рандеву'
    },
    {
        'policy_number': '98-76 5432-10',
        'format_number': '1101101111011',
        'type_of_insurance': OMS,
        'expiration_date': '24.11.2023',
        'company': 'СК Рандеву'
    },
    {
        'policy_number': '12-341234-5678',
        'format_number': '11011111101111',
        'type_of_insurance': DMS,
        'expiration_date': '25.11.2024',
        'company': 'Страх-трах'
    },
    {
        'policy_number': '9876-543210',
        'format_number': '11110111111',
        'type_of_insurance': OMS,
        'expiration_date': '26.11.2025',
        'company': 'Страх-трах'
    }
]


class Command(BaseCommand):
    help = 'Database initialization'
    
    def handle(self, *args, **options):
        try:
            user = User.objects.get(username="tech")
        except models.ObjectDoesNotExist:
            user = User.objects.create(username="tech", password="password", email="email@mail.ru")
            user.save()
        
        if InsuranceCompany.objects.exists():
            return
        
        objs = [
            InsuranceCompany(
                title=company['title'],
                phone=company['phone'],
                created_by=user,
                updated_by=user
            )
            for company in companies
        ]
        
        InsuranceCompany.objects.bulk_create(objs)
        
        if InsuranceData.objects.exists():
            return
        
        objs_data = [
            InsuranceData(
                policy_number=data['policy_number'],
                format_number=data['format_number'],
                type_of_insurance=data['type_of_insurance'],
                expiration_date=datetime.strptime(data['expiration_date'], '%d.%m.%Y').date(),
                company=InsuranceCompany.objects.get(title=data['company']),
                created_by=user,
                updated_by=user
            )
            for data in company_data
        ]
        
        InsuranceData.objects.bulk_create(objs_data)