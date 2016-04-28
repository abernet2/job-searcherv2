from django.contrib import admin

from .models.job_post import JobPost
from .models.company import Company

admin.site.register(JobPost)
admin.site.register(Company)