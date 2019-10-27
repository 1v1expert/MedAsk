from django.shortcuts import render
from django.http import HttpResponse


def home_view(request) -> HttpResponse:

    # manufacturers = Manufacturer.objects.all()
    return render(request, 'index.html', {
        'manufacturers': 'ss'#manufacturers,
        # 'feedback': feedback_form,
        # 'auth_form': auth_form,
        # 'reg_form': reg_form,
        # 'subscribe_form': subscribe_form,
        # 'error': error
    })