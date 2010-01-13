"""Utils for easy_extract"""
CHAR_TO_ESCAPE = (' ', '(', ')', '*', "'", '"', '&')

def get_filename_name(filename):
    return filename.split('.')[0]

def escape_filename(filename):
    for char in CHAR_TO_ESCAPE:
        filename = filename.replace(char, '\%s' % char)
    return filename
