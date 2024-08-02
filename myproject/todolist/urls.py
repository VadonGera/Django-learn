from django.urls import path
from .views import (
    base,
    TodolistViewSet,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
)
from rest_framework.routers import DefaultRouter


app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TodolistViewSet)


urlpatterns = [
    path('', base, name='base'),
    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),
] + router.urls
