from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(models.ForeignKey(User, on_delete=models.DO_NOTHING))
    date = models.DateTimeField(default=datetime.now, blank=True)
    content = models.CharField(default="", max_length=5000)
