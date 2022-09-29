from django.contrib import admin
from django.urls import path

from to_do.views.tasks import index_view, add_task_view, task_view, task_edit_view, confirmation_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('tasks/confirmation/<int:pk>', confirmation_view, name='delete_confirmation'),
    path('tasks/add/', add_task_view, name='task_add'),
    path('tasks/<int:pk>', task_view, name='task_detail'),
    path('edit/', task_view, name='task_edit'),
    path('tasks/edit/<int:pk>', task_edit_view, name='task_edit'),
]
