from django.conf.urls import url
from app.views import home_view, api_check_policy_number

# app_name = 'app'
urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'api/check_policy', api_check_policy_number, name='check_policy')
]
