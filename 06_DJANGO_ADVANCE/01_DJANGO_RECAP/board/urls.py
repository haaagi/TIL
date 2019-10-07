from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name ='index'), # /board/
    # Read 글 목록  render
    path('articles/', views.list, name='list'),
    # Read글 상세 render
    path('articles/<int:id>/', views.detail, name='detail'),
    # Create 글 쓰기 render
    path('articles/new/', views.new, name='new'),
    # Create글 저장
    path('articles/create/', views.create, name='create'),
    # Update 글 수정 render
    path('articles/<int:id>/edit/', views.edit, name='edit'),
    # Update 글 실제수정
    path('articles/<int:id>/update/', views.update, name='update'),
    # Delete 글 삭제
    path('articles/<int:id>/delete/', views.delete, name='delete'),
]