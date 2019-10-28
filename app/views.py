from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json

from app.models import InsuranceData
from app.util import formalize_police_number


def home_view(request) -> HttpResponse:
    return render(request, 'index.html', {})


@csrf_exempt
def api_check_policy_number(request) -> HttpResponse:
    if request.method == 'POST':
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        policy_number = body.get('policy_number')
        
        if policy_number and len(policy_number):
            format_policy = formalize_police_number(policy_number)
            
            try:
                insurance = InsuranceData.objects.get(format_number=format_policy)
                return JsonResponse({"OK": True, 'result': insurance.to_json()}, content_type='application/json')
            except (InsuranceData.DoesNotExist, InsuranceData.MultipleObjectsReturned):
                return JsonResponse({"OK": False}, content_type='application/json')
            # return JsonResponse(
            #     {"results": list(InsuranceData.objects.values('type_of_insurance',
            #                                                   'expiration_date',
            #                                                   'company__title',
            #                                                   'company__phone'))}, content_type='application/json')
        # body = str(request.body)
        # print(body)
        return JsonResponse({"OK": False}, content_type='application/json')
        
    return HttpResponseNotAllowed()


