from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    # Read글 상세 render
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    # Create 글 쓰기 render
    path('articles/new/', views.new_article, name='new_article'),
    # Update 글 수정 render
    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    # Delete 글 삭제
    path('articles/<int:article_id>/delete/', views.delete_article, name='delete_article'),

    # Commnet create
    path('articles/<int:article_id>/comments/new/', views.new_comment, name='new_comment'),
]