from os import listdir
from os.path import isfile, join, dirname

import models as m

from job_post import JobPost

BASE = "http://www.builtinchicago.org/job/"
url = lambda title: BASE + title

def seed():
    posts = JobPost.all()
    for post in posts:
        try:
            make_models(post)
        except:
            print "Oops theres an error at"

def make_models(post):
    comp = m.Company.objects.get_or_create(name=post.company)[0]
    print(post)
    comp.save()
    try:
        jp = m.JobPost.objects.get_or_create(url=url(post.title),
                    position=post.position,
                    company=comp )[0]
        jp.save()
    except:
        print "Oops theres an error at" + url(post.title)    
        return

    for h in post.content:
        ph = m.PostHeader.objects.get_or_create(orig_header=h, job_post=jp)[0]
        ph.save()
        if type(post.content[h]) == list:
            for c in post.content[h]:
                cont = m.Content.objects.get_or_create(text=c.encode('utf-8'), post_header=ph)[0]
                cont.save()
        else:
            cont = m.Content(text=post.content[h], post_header=ph)
            cont.save()

    return jp




if __name__ == '__main__':
    seed()