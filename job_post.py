import re
import os
from helpers import write, gets, titleize
from header_puller import header_puller as pull

DIR = 'cached_job_posts/'
class JobPost:
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.company = kwargs['company']
        self.post = kwargs['post']
        self.position = kwargs['position']
        
    def save_cache(self, attrs={}):
        f = self.file_name()
        attrs['title'] = self.title
        attrs['company'] = self.company
        attrs['post'] = self.post
        attrs['position'] = self.position
        write(attrs, f)

    def file_name(self):
        return DIR + self.title + '.txt'

    def headers(self):
        return pull(self.post).keys()

    @classmethod
    def all(cls):
        return [JobPost.load_cache(f) for f in os.listdir(DIR) if '.txt' in f]

    @classmethod
    def load_cache(cls, file, dire=DIR):
        construct = cls == JobPost # if other classes call, we don't want to call the constructor
        file = normalize(file, dire)
        raw = gets(file)
        if not raw:
            return none
        match = re.split(r'#position|#post|#company', raw)
        attrs = {'title': titleize(file)}
        attrs['position'] = match[1].strip()
        attrs['company'] = match[2].strip()
        attrs['post'] = match[3].strip()
        return cls(**attrs) if construct else attrs

def normalize(file, dire):
    if dire not in file:
        file = dire + file
    if '.txt' not in file:
        file = file + '.txt'
    return file

if __name__ == '__main__':
    # j = JobPost(company='c', post='p', position='pos', title='t')
    j = JobPost.load_cache(DIR + 'android-developer-26.txt')
    print(j.headers())