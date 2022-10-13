from django.urls import path
from todolist.views import add_task, add_task_ajax, create_task_modal, delete, set_status, show_json, show_todolist, register, login_user, logout_user, todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_todolist'),
    path('delete/<int:id>', delete, name='delete'),
    path('toggle/<int:id>', set_status, name='toggle'),
    path('todolist_ajax/', show_json, name='show_json'),
    path('json/', todolist_ajax, name='todolist_ajax'),
    path('add/', create_task_modal, name='add'),
]