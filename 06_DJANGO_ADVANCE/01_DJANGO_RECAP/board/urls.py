from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name ='index'), # /board/
    # Read 글 목록  render
    path('articles/', views.list, name='list'),
    # Read글 상세 render
    path('articles/<int:id>/', views.detail, name='detail')
    # Create 글 쓰기 render
    # Create글 저장

    # Update 글 수정 render
    # Update 글 실제수정

    # Delete 글 삭제
]