from rest_framework import serializers

from todolist.models import Task, Comment, Tag

# Сериализатор для тегов Tag
class TegSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name']


# Сериализатор для задач Task
class TaskSerializer(serializers.ModelSerializer):
    # Создаем новое поле - кол-во тегов задачи
    # tags_count = serializers.SerializerMethodField()
    tags_count = serializers.IntegerField(source='tags.all.count')
    tags = TegSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        # fields = '__all__'
        exclude = ['owner']

    # Вычисляем новое поле по правилам def get_<имя поля>
    # obj - наш объект Task
    # def get_tags_count(self, obj):
    #     return obj.tags.all().count()

# Сериализатор для комментариев Comment
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['task', 'comment']

    # Валидация на уровне поля comment
    def validate_comment(self, value):
        if 'bad' in value:
            raise serializers.ValidationError("недопустимое слово 'bad'")
        return value

    # Валидация на уровне объекта comment
    def validate(self, data):
        if 'word' in data['comment']:
            raise serializers.ValidationError("недопустимое слово 'word'")
        return data
