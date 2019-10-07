from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('guess/', views.guess, name='guess'),  # HOST/home/hi/
    path('', views.index, name='index'),  # HOST/home/ 아무것도 없기 때문에
    path('answer/', views.answer, name='answer') #home/answer
]