from string import ascii_lowercase as ascii_lowercase
from random import choice
class Cipher:
    def __init__(self, key=None):
        if not key:
            self.key = ''.join([choice(ascii_lowercase) for i in range(100)])
        else:
            self.key = key
        self.shift = [ascii_lowercase.index(i) for i in self.key]

    def encode(self, text):
        text = text.lower()
        return ''.join([ascii_lowercase[(ascii_lowercase.index(j)+self.shift[i%len(self.key)])%26]for i,j in enumerate(text)])

    def decode(self, text):
        text = text.lower()
        return ''.join([ascii_lowercase[(ascii_lowercase.index(j)-self.shift[i%len(self.key)])%26]for i,j in enumerate(text)])

