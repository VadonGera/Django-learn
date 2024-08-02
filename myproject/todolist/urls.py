from django.urls import path
from .views import (
    base,
    TodolistViewSet,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
)
from rest_framework.routers import DefaultRouter

from todolist.apps import TodolistConfig

# app_name = 'tasks'
app_name = TodolistConfig.name

router = DefaultRouter()
router.register('tasks', TodolistViewSet)


urlpatterns = [
    path('', base, name='base'),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
] + router.urls
