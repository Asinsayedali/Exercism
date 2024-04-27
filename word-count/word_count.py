import re
from collections import Counter


def count_words(sentence):
    return Counter(re.findall(r"([a-z\d]+(?:'[a-z\d]+)?)", sentence.lower()))
