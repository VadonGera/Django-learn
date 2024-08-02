from rest_framework import serializers

from todolist.models import Task, Comment


# Сериализатор для задач Task
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


# Сериализатор для комментариев Comment
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
