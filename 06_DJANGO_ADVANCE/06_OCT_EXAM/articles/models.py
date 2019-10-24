from django.db import models
from django.conf import settings  # 만약 import 되있다면 
from django.contrib.auth import get_user_model  # 이게 중요한거다~1!!!


User = get_user_model()
class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 내가 뭐라고 접근할지 -> ...related_name= 남이 나를 뭐라고 부를지
    like_users = models.ManyToManyField(User, related_name='like_articles')
