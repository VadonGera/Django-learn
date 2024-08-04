from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from todolist.models import Task, Comment
from todolist.serializers import TaskSerializer, CommentSerializer
from rest_framework import permissions

context = 'user@main - my variable'


def base(request):
    """Base view"""
    return render(
        request,
        'todolist/base.html',
        context={'variable': context},
    )


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Проверяем, что пользователь является владельцем объекта или является членом персонала.
        return obj.owner == request.user or request.user.is_staff


# Контроллер для модели Task через ViewSet
class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    # permission_classes = [IsOwner]

    def perform_update(self, serializer):
        if not serializer.instance.owner == self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой задачи или членом персонала.")
        serializer.save()


# Контроллер для Comment (для просмотра списка и создания объекта) через Generic
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


# Контроллер для Comment (для просмотра, редактирования (PUT и PATCH), удаления объекта) через Generic
class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    # Можно переопределять методы, но надо еще разбираться.
    # def perform_destroy(self, instance):
    #     instance.is_active = False
    #     instance.save()
