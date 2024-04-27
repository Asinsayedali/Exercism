import re


def abbreviate(words):
    return ''.join(item[0].upper() for item in re.findall(r"[a-zA-Z']+", words))
