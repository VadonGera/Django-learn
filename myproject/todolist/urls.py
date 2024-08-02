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
router.register('api/tasks', TodolistViewSet)


urlpatterns = [
    path('', base, name='base'),
    path('api/comments/', CommentListCreateAPIView.as_view()),
    path('api/comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
] + router.urls
