from django.contrib import admin
from app.models import InsuranceData, InsuranceCompany


admin.site.register(InsuranceCompany)
admin.site.register(InsuranceData, )