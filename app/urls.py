from django.contrib import admin
from django.urls import path
from .views.task_views import *
from .views.user_views import *

urlpatterns = [
    path('', task_list, name=''),
    path('task_list/', task_list, name='task_list'),
    path('register_task/', register_task, name='register_task'),
    path('edit_task/<int:id>', edit_task, name='edit_task'),
    path('remove_task/<int:id>', remove_task, name='remove_task'),
    path('signup/', signup_user, name='signup'),
    path('signin/', signin_user, name='signin'),
    path('signout/', signout_user, name='signout'),
]

