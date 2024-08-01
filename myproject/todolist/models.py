from django.db import models

class Task(models.Model):

    name = models.CharField(max_length=150, verbose_name='Тема задачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
