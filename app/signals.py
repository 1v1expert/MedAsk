# -*- coding: utf-8 -*-

from django.db.models import signals  # NOQA
from django.dispatch import receiver

from app.models import InsuranceData
from app.util import formalize_police_number


@receiver(signals.pre_save, sender=InsuranceData)
def pre_insurance_data_save(sender, instance, *args, **kwargs):
    instance.format_number = formalize_police_number(instance.policy_number)