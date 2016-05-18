from urllib2 import urlopen
from bs4 import BeautifulSoup

import builtin_parser as bp

BASE = "http://www.builtinchicago.org"
QUERY = "/jobs?category=developer-engineer-78"

def get_paths():
    url = BASE + QUERY
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    job_titles = soup.find_all('div',{"class": "job-title"})
    paths = [BASE + job.find('a')['href'] for job in job_titles]
    return paths

def scrape():
    paths = get_paths()
    pages = [bp.parse(path) for path in paths]
    return pages

if __name__ == '__main__':
    pages = scrape()
    for page in pages:
        page.save()
        print(page)