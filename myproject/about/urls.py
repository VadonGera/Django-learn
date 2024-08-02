from django.urls import path
from .views import about
from about.apps import AboutConfig

app_name = AboutConfig.name

urlpatterns = [
    path('', about, name='about'),
]