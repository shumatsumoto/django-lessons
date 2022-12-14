from django.db import models
from django.utils import timezone


class Category(models.Model):
  name = models.CharField('カテゴリ名', max_length=255)
  def __str__(self):
    return self.name


class Post(models.Model):
  title = models.CharField('title', max_length=255)
  text = models.TextField('本文')
  created_at = models.DateTimeField('作成日', default=timezone.now)
  category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
  def __str__(self):
    return self.title