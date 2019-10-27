from django.conf.urls import url
from django.contrib import admin
from app.views import home_view

app_name = 'app'
urlpatterns = [
    url(r'^$', home_view, name='home')
]
