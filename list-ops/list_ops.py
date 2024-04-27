def append(list1, list2):
    list1 += list2
    return list1


def concat(lists):
    return [x for lst in lists for x in lst]


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    count = 0
    for element in list:
        count += 1
    return count


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    for x in list:
        initial = function(initial,x)
    return initial


def foldr(function, list, initial):
    for x in list[::-1]:
        initial = function(initial, x)
    return initial


def reverse(list_1):
    return list_1[::-1]
