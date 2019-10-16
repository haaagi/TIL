from django.db import models
from django.urls import reverse

# Create your models here.

"""
$ python manage.py migrate <APP_NAME> zero
$ rm <APP_NAME>/migrations/0*  => 이거하면 0으로 시작하는 migrations 있는 파일 삭제 전부다
"""

class Posting(models.Model):
    content = models.TextField()
    icon = models.CharField(max_length=30, default='')
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):  # detail page 있으면 이거 쓰자.
        return reverse("sns:posting_detail", kwargs={"posting_id": self.pk})
    

    def __str__(self):
        return f'{self.pk}:{self.content[:10]}'


