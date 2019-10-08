from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('student/', views.list, name='list'),
    path('student/new/', views.new, name='new'),
    path('student/create/', views.create, name="create"),
    # create
    # edit
    path('student/<int:id>/edit/', views.edit, name="edit"),
    path('student/<int:id>/update/', views.update, name="update"),
    path('student/<int:id>/delete/', views.delete, name="delete"),
    path('student/detail/<int:id>/', views.detail, name="detail"),
    # update
    # delete
]
