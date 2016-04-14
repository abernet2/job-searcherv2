from job_post import JobPost
from helpers import clean
import contains

def load_all_headers():
    posts = JobPost.all()
    headers = [format_header(h, post) for post in posts for h in post.headers()]
    return headers

def format_header(h, post):
    h = h.replace(post.company.upper(), '<COMPANY>')
    h = h.replace(post.position.upper(), '<POSITION>')
    return clean(h)

def feature_extractor(h):
    fs = [int(feature(h)) for feature in contains.features]
    return fs

def extract_all_features(headers=None):
    headers = load_all_headers() if headers == None else headers
    return [feature_extractor(h) for h in headers]

if __name__ == '__main__':
    print(extract_all_features())