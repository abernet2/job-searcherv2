def company(h):
    words = ['US', 'WE', 'COMPANY']
    return check_words(h, words)

def about(h):
    return 'ABOUT' in h

def qualifications(h):
    return 'QUALIF' in h

def experience(h):
    return 'EXPERIENCE' in h

def responsibilities(h):
    return 'RESPONSI' in h

def you(h):
    return 'YOU' in h

def extra(h):
    words = ['EXTRA', 'NICE', 'PREFER', 'BONUS']
    return check_words(h, words)

def position(h):
    words = ['JOB', 'POSITION', 'GIG']
    return check_words(h, words)

features = [company, about, qualifications, experience, responsibilities, you, extra, position]

def check_words(string, words):
    return any(w in string for w in words)