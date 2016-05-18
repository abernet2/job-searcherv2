import os
from bs4 import BeautifulSoup
from helpers.utils import gets, puts, find_span, write, titleize, is_url, clean_company, clean_position

import seed
from job_post import JobPost 

def parse(url):
    attrs = extract(gets(url))
    attrs['title'] = titleize(url)
    post = JobPost(attrs)
    return seed.make_models(post)

def extract(html, attrs={}):
    soup = BeautifulSoup(html, 'html.parser')
    attrs['company'] = clean_company(find_span(soup, 'nc-fallback-title'))
    attrs['position'] = find_span(soup, 'nj-job-title')
    attrs['post'] = unicode(soup.find('span', {'class': 'nj-job-body'}))
    return attrs

if __name__ == '__main__':
    page = parse("http://www.builtinchicago.org/job/account-executive-getaways")
    print(page.company)