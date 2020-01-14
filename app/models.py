from django.db import models

# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=30)
    trust = models.IntegerField(default=1)

class Runking(models.Model):
    User = models.ForeignKey(User,models.CASCADE)
    point = models.IntegerField(default=0)

class Image_list(models.Model):
    image_path = models.CharField(max_length=100,null=True)
    cate = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)
    correct = models.IntegerField(default=-1)

class Cate(models.Model):
    cate = models.CharField(max_length=30)

class Sub(models.Model):
    cate = models.CharField(max_length=30)
    sub = models.CharField(max_length=30)

