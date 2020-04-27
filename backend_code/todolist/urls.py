from django.urls import path
from . import  views

app_name = 'todolist'
urlpatterns = [
    path('', views.ToDo.as_view(), name='待办事项'),
    path('/<str:id>', views.ToDoDelete.as_view(), name='删除待办事项')
]
