from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from ..models import content as models

@csrf_exempt
def single(request, content_id):
    content = models.Content.objects.get(id=content_id)
    if request.method == 'DELETE':
        post = content.post_header.job_post
        return HttpResponseRedirect('/job_post/{}'.format(post.id))
    return HttpResponse('render(request, , context)')

def edit(request, content_id):
    content = models.Content.objects.get(id=content_id)
    if request.method == 'GET':
        context = {
            'text': content.text,
        }
        return HttpResponse(render(request, 'content/edit.html', context))
