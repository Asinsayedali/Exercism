import re


def cipher_text(plain_text):
    result = str()
    cleaned = re.sub(r"[^\w\s]", "", plain_text).replace(" ", "")
    cleaned = cleaned.lower()
    r = round(len(cleaned) ** 0.5)
    if len(cleaned) > r * r:
        c = r + 1
    else:
        c = r
    if len(cleaned) == 0: return ""
    for pos in range(c):
        for step in range(r):
            try:
                result += cleaned[pos + step * c]
            except :
                result += ' '
        result += ' '
    return result[:-1]
