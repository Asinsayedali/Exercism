from string import ascii_lowercase
Encoding = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(plain_text):
    result = ''.join(char for char in plain_text.lower() if char.isalnum())
    return ' '.join(result[index:index+5] for index in range(0, len(result), 5)).translate(Encoding)


def decode(ciphered_text):
    return ''.join(char for char in ciphered_text if char.isalnum()).translate(Encoding)

