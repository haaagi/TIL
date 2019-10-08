from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def get_absolute_url(self):
        return reverse("board:detail", kwargs={"id": self.pk})
