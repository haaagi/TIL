from django.urls import path
from . import views

app_name = 'todos'   #  필요 없음 . 

urlpatterns = [
    path('', views.create_todo),
    path('<int:todo_id>/', views.update_delete_todo)    # PATCH 방식 api/v1/todos/1 => update 1 || DELETE api/v1/todos/1 => Delete 1
]
