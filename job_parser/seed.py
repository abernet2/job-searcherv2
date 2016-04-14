import models as m

from builtin_post import BuiltinPost

BASE = "http://www.builtinchicago.org/job/"
url = lambda title: BASE + title

def seed():
    posts = BuiltinPost.all()
    for post in posts:
        make_models(post)

def make_models(post):
    comp = m.Company(name=post.company)
    comp.save()
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