def is_isogram(string):
    list1=string.lower().replace(" ","").replace("-","")
    return len(list1)==len(set(list1))