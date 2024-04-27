def is_pangram(sentence):
    sentence=sentence.lower()
    list=set()
    for char in sentence:
        if char.isalpha():
            list.add(char)
    if len(list)==26:
        return True
    else:
        return False
