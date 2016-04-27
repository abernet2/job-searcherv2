from __future__ import unicode_literals

from django.db import models

class PostHeader(models.Model):
    orig_header = models.CharField(max_length=200)
    job_post = models.ForeignKey('JobPost')
    def __str__(self):
        return self.orig_header