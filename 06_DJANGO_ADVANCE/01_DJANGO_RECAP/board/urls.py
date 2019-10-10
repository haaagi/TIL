from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('articles/', views.list, name='list'),
    # Read글 상세 render
    path('articles/<int:id>/', views.detail, name='detail'),
    # Create 글 쓰기 render
    path('articles/new/', views.new, name='new'),
    # Update 글 수정 render
    path('articles/<int:id>/edit/', views.edit, name='edit'),
    # Delete 글 삭제
    path('articles/<int:id>/delete/', views.delete, name='delete'),
]