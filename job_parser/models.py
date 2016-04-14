from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)

class JobPost(models.Model):
    url = models.CharField(max_length=200)
    position = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Content(models.Model):
    text = models.CharField(max_length=1000)
    post_header = models.ForeignKey(PostHeader, on_delete=models.CASCADE)

# will eventually add a foreign key for headers
class PostHeader(models.Model):
    orig_header = models.CharField(max_length=200)
    post = models.ForeignKey(JobPost, on_delete=models.CASCADE)