
def square(number):

    t = 1
    if number > 64 or number <= 0:
        raise ValueError("square must be between 1 and 64")
    else:
        for i in range(1, number):
            t = t*2

    return t


def total():
    result = 1
    t = 1
    for i in range(1,64):
        t = t*2
        result = result + t

    return result
