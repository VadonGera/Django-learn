from django.urls import path
from .views import base, TodolistViewSet
from rest_framework.routers import DefaultRouter


app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TodolistViewSet)


urlpatterns = [
    path('', base, name='base'),
] + router.urls
