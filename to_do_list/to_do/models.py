from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    NEW = 'New', 'Новая'


class Task(models.Model):
    task_text = models.CharField(verbose_name='Название задачи', max_length=200, null=False, blank=False)
    task_description = models.TextField(verbose_name='Текст', max_length=3000, null=False, blank=False)
    state = models.CharField(verbose_name='Статус', choices=StatusChoices.choices, max_length=100,
                             default=StatusChoices.NEW)
    deadline = models.DateTimeField(verbose_name='Дедлайн', null=True, default=None)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.task_text} {self.state} {self.deadline}'
