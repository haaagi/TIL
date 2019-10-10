from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("board:article_detail", kwargs={"article_id": self.pk})


class Comment(models.Model):
    content = models.CharField(max_length=200)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # CASCADE는 원 글이 삭제되면 코맨트를 같이 삭제하겠다는 말.


