from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class JobPost(models.Model):
    url = models.CharField(max_length=200, unique=True)
    position = models.CharField(max_length=150)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.position

# will eventually add a foreign key for headers
class PostHeader(models.Model):
    orig_header = models.CharField(max_length=200)
    job_post = models.ForeignKey(JobPost)
    def __str__(self):
        return self.orig_header

class Content(models.Model):
    text = models.CharField(max_length=1000)
    post_header = models.ForeignKey(PostHeader, on_delete=models.CASCADE)