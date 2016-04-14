import os
from bs4 import BeautifulSoup
from helpers import gets, puts, find_span, write, titleize, is_url, clean_company, clean_position
from job_post import JobPost

class BuiltinPost(JobPost):
    def __init__(self, html, title):
        attrs = {'title': title}
        attrs = extract(html, attrs)
        JobPost.__init__(self, **attrs)

    @classmethod
    def parse(cls, url):
        return BuiltinPost(gets(url), titleize(url)) 

def extract(html, attrs={}):
    soup = BeautifulSoup(html, 'html.parser')
    attrs['company'] = clean_company(find_span(soup, 'nc-fallback-title'))
    attrs['position'] = find_span(soup, 'nj-job-title')
    attrs['post'] = unicode(soup.find('span', {'class': 'nj-job-body'}))
    return attrs

def checked_url(str):
    cache = BuiltinPost.load_cache(titleize(str))
    return False if cache else is_url(str)

# def clean_company(company):


if __name__ == '__main__':
    print(clean_company('Raise.com'))
