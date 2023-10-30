from django.db import models

# Create your models here.
class Url(models.Model):
    short_url=models.TextField(max_length=6,unique=True)
    long_url=models.TextField(max_length=100,unique=True)