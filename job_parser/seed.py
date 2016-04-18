import models as m

from job_post import JobPost

BASE = "http://www.builtinchicago.org/job/"
url = lambda title: BASE + title

def seed():
    posts = JobPost.all()
    for post in posts:
        make_models(post)

def make_models(post):
    comp = m.Company.objects.get_or_create(name=post.company)[0]
    print(comp)
    # comp.save()
    jp = m.JobPost(url=url(post.title),
                    position=post.position,
                    company=comp )
    jp.save()

    for h in post.content:
        ph = m.PostHeader(orig_header=h, post=jp)
        ph.save()
        cont = m.Content(text=post.content[h], post_header=ph)
        cont.save()


if __name__ == '__main__':
    seed()