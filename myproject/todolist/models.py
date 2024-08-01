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

    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
