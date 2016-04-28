from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
