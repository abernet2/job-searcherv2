from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from ..builtin_scraper import scrape

from ..models import job_post as models

# Create your views here.
def index(request):
    posts = models.JobPost.objects.all().order_by('created_at')
    context = {
        'posts': posts,
    }
    return HttpResponse(render(request, 'job_post/index.html', context))

@csrf_exempt
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

@csrf_exempt
def fetch(request):
    # pages = scrape()
    pages = models.JobPost.objects.get(id=4)
    context = {
        'pages': pages,
    }
    if request.is_ajax():
        return HttpResponse(json.dumps(pages, default=dictify))
    return HttpResponse(render(request, 'job_post/fetch.html', context))

def dictify(post):
    if post:
        return {
            'url': post.url,
            'position': post.position,
            'company': post.company.name,
            'id': post.id
        }