from django.shortcuts import render
from rest_framework import viewsets
from todolist.models import Task
from todolist.serializers import TaskSerializer


def base(request):
    return render(request, 'todolist/base.html')


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
