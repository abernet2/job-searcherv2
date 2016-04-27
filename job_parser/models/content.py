from __future__ import unicode_literals

from django.db import models

class Content(models.Model):
    text = models.CharField(max_length=1000)
    post_header = models.ForeignKey('PostHeader', on_delete=models.CASCADE)