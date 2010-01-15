"""Utils for easy_extract"""

CHAR_TO_ESCAPE = (' ', '(', ')', '*', "'", '"', '&')

def get_filename_name(filename):
    names = filename.split('.')
    if len(names) > 3:
        return '.'.join(names[:-2])
    return names[0]

def escape_filename(filename):
    for char in CHAR_TO_ESCAPE:
        filename = filename.replace(char, '\%s' % char)
    return filename
