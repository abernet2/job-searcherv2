import re
from urllib2 import urlopen

def gets(file_name):
    if is_url(file_name):
        io = urlopen(file_name)
    else:
        io = open(file_name, 'r')
    result = io.read().decode('utf-8') if io else None
    io.close()
    return result

def write(dict, file_name):
    f = open(file_name, 'w')
    for key in dict.keys():
        f.write('\n\n#' + key +'\n')
        f.write(dict[key].encode('utf=8'))

def puts(thing):
    thing = thing.encode('utf-8')
    print(thing)
    return thing

def find_span(soup, _class):
    return soup.find('span', {'class': _class}).text.strip()

def clean(str):
    str = re.sub(r'\s+', r' ', str)
    return re.sub(r'[.,]+', r'', str)

def titleize(str):
    str = str.split('/')[-1]
    return re.sub('.txt', '', str)

def is_url(s):
    return 'http' in s

def headerify(h):
    last_sent = h.split('.')[-1]
    return last_sent.strip().replace(':', '').upper()

def clean_company(company):
    return re.split(r'[,.()]', company)[0]

def clean_position(pos):
    return re.sub(r'-', ' ', pos)