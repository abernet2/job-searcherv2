from bs4 import BeautifulSoup
import re
from helpers import headerify, gets

def header_puller(html):
    html = collapse_html(html)
    soup = BeautifulSoup(html, 'html.parser')
    content = {}
    pull_lists(soup.find_all('ul'), content)
    pull_special_tags(soup, content)
    return content

def pull_lists(lists, content):
    for ul in lists:
        sib = ul.find_previous_sibling()
        h = headerify(sib.text) if sib else ''
        if len(h) == 0:
            return
        lis = ul.contents
        content[h] = [l.text for l in lis if(hasattr(l, 'text'))]

def pull_special_tags(s, content):
    tags = ['b', 'u', 'strong']
    for tag in tags:
        pull_tag(tag, s, content)
    return content

def pull_tag(tag, s, content):
    for tag in s.find_all(tag):
        h = headerify(tag.text)
        if len(h) == 0:
            return
        sib = tag.find_next_sibling()
        if not sib:
            tag = tag.find_parent()
            sib = tag.find_next_sibling()
        fill_content(h, sib, content)
        

def fill_content(header, sib_tag, content):
    if not sib_tag or header in content.keys() or not sib_tag.text:
        return
    if sib_tag.children:
        content[header] = [condense(child.text) for child in sib_tag.children if(hasattr(child, 'text'))]
    if len(content[header]) is 0:
        content[header] = condense(sib_tag.text).encode('utf-8')

def collapse_html(html):
    html = html.replace('\n\s*', '')
    html = html.replace('<br/>', '')
    html = re.sub(r'>\s+', '>', html)
    html = re.sub(r'\s+<', '<', html)
    return html

def condense(text):
    return re.sub(r'\n\s*', r'\n', text.strip())

if __name__ == '__main__':
    filename = 'cached_job_posts/advanced-software-engineer-test.txt'
    html = gets(filename)
    html = html.split('#post')[1].strip()
    print(header_puller(html))
