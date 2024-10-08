from django.db import models


class Task(models.Model):
    STATUS_DRAFT = 'DRAFT'
    STATUS_PUBLISHED = 'PUBLISHED'

    STATUSES = (
        (STATUS_DRAFT, 'Черновик'),
        (STATUS_PUBLISHED, 'Опубликована'),
    )

    name = models.CharField(max_length=150, verbose_name='Тема задачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    status = models.CharField(choices=STATUSES, default=STATUS_DRAFT, verbose_name='Статус', max_length=10)
    owner = models.CharField(max_length=50, default='anonim', verbose_name='Владелец')
    tags = models.ManyToManyField('todolist.Tag', verbose_name='теги', related_name='tasks')

    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')

    comment = models.CharField(max_length=255, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.comment


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название тега')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name
