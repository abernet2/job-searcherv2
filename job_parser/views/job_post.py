from django.shortcuts import render
from django.http import HttpResponse

from ..models import job_post as models

# Create your views here.
def index(request):
    posts = models.JobPost.objects.all()
    context = {
        'posts': posts,
    }
    return HttpResponse(render(request, 'job_post/index.html', context))

def show(request, job_post_id):
    post = models.JobPost.objects.get(id=job_post_id)
    context = {
        'post': post,
        'headers': post.postheader_set.all(),
    }
    return HttpResponse(render(request, 'job_post/show.html', context))

def edit(request, job_post_id):
    post = models.JobPost.objects.get(id=job_post_id)
    context = {
        'post': post,
    }
    return HttpResponse(render(request, 'job_post/edit.html', context))