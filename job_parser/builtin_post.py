import os
from bs4 import BeautifulSoup
from helpers.utils import gets, puts, find_span, write, titleize, is_url, clean_company, clean_position
from job_post import JobPost

def parse_built_in(url):
    attrs = extract(gets(url))
    attrs['title'] = titleize(url)
    return JobPost(attrs)

def parse(url):
    return BuiltinPost(gets(url), titleize(url)) 

def extract(html, attrs={}):
    soup = BeautifulSoup(html, 'html.parser')
    attrs['company'] = clean_company(find_span(soup, 'nc-fallback-title'))
    attrs['position'] = find_span(soup, 'nj-job-title')
    attrs['post'] = unicode(soup.find('span', {'class': 'nj-job-body'}))
    return attrs

if __name__ == '__main__':
    page = parse_built_in("http://www.builtinchicago.org/job/account-executive-getaways")
    print(page)