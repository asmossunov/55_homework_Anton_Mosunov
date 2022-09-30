from django.contrib import admin
from django.urls import path

from to_do.views.tasks import index_view, add_task_view, task_view, task_edit_view, delete_view, confirm_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('task/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
    path('task/<int:pk>/delete/', delete_view, name='task_delete'),
    path('tasks/add/', add_task_view, name='task_add'),
    path('tasks/<int:pk>', task_view, name='task_detail'),
    path('tasks/<int:pk>/edit/', task_edit_view, name='task_edit'),
]
