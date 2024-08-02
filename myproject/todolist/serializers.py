from rest_framework import serializers

from todolist.models import Task, Comment


# Сериализатор для задач Task
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['owner']


# Сериализатор для комментариев Comment
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['task', 'comment']

    def validate_comment(self, value):
        if 'bad' in value:
            raise serializers.ValidationError("недопустимое слово 'bad'")
        return value
