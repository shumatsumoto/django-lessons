from django.db import models
from django.utils import timezone


class Post(models.Model):
  title = models.CharField('title', max_length=255)
  text = models.TextField('本文')
  created_at = models.DateTimeField('作成日', default=timezone.now)