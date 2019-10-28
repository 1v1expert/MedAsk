from django.db import models
from django.contrib.auth.models import User
from .choices import TYPES
# import uuid


class Base(models.Model):
    """
    Абстрактная базовая модель
    """
    # uid = models.UUIDField(verbose_name="Идентификатор", primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Когда создано")
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Кем создано", editable=False, related_name="+")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Когда обновлено")
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Кем обновлено", editable=False, related_name="+")
    is_public = models.BooleanField("Опубликовано?", default=True)
    deleted = models.BooleanField("В архиве?", default=False, editable=False)
    
    class Meta:
        abstract = True
        verbose_name = "Базовая модель "
        verbose_name_plural = "Базовые модели"


class InsuranceCompany(Base):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cover = models.ImageField(upload_to='images/', null=True)
    
    class Meta:
        verbose_name = "Страховая компания"
        verbose_name_plural = "Страховые компании"
    
    def __str__(self):
        return self.title

        
class InsuranceData(Base):
    policy_number = models.CharField(verbose_name='Номер СП', max_length=255)
    format_number = models.CharField(verbose_name='Формат СП', default=None, max_length=255)
    type_of_insurance = models.CharField(max_length=4, choices=TYPES, verbose_name="Тип страхования")
    expiration_date = models.DateField(verbose_name='Дата окончания')
    company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE)
    
    def to_json(self):
        return dict(
            type_of_insurance=self.type_of_insurance,
            expiration_date=self.expiration_date,
            company_title=self.company.title,
            company_phone=self.company.phone,
            img=self.company.cover.url
        )
    
    class Meta:
        verbose_name = "Данные по СК"
    
    def __str__(self):
        return 'Policy number: {}'.format(self.policy_number)
