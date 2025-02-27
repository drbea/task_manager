from django.urls import path
from . import views
app_name = "task"

urlpatterns = [
  path("", views.index, name = "index"),
  path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
  path('task_by_user/<int:user_id>', views.task_by_user, name='task_by_user'),

 path('add/', views.add_task, name='add_task'),
 path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]
