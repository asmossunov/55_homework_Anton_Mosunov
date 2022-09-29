from django.contrib import admin

from to_do.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_text', 'state', 'deadline')
    list_filter = ('id', 'task_text', 'state', 'deadline')
    search_fields = ('id', 'task_text', 'state', 'deadline')
    fields = ('id', 'task_text', 'state', 'deadline')
    readonly_fields = ['id']


admin.site.register(Task, TaskAdmin)
