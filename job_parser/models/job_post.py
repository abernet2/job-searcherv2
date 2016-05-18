from __future__ import unicode_literals

from django.db import models

class JobPost(models.Model):
    url = models.CharField(max_length=200, unique=True)
    position = models.CharField(max_length=150)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position