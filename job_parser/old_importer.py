import os
from builtin_post import BuiltinPost
from helpers.utils import gets, titleize

OLD_DIR = 'cached_pages/'
NEW_DIR = 'cached_job_posts/'

def load_directory():
    for f in os.listdir(OLD_DIR):
        import_file(f)

def import_file(filename):
    html = gets(OLD_DIR + filename)
    bip = BuiltinPost(html, titleize(filename))
    bip.save_cache()
    

if __name__ == '__main__':
    load_directory()