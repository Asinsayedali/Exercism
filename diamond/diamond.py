from string import ascii_uppercase


def rows(letter):
    index = ascii_uppercase.index(letter)
    diamond_list = []

    for i in range(0, index + 1):
        if i == 0:
            spaced_letter = " " * (index - i) + ascii_uppercase[i] + " " * (index - i)
        else:
            spaced_letter = " " * (index - i) + ascii_uppercase[i] + " " * (2 * i - 1) + ascii_uppercase[i] + " " * (index - i)
        diamond_list.append(spaced_letter)

    return diamond_list[:-1] + diamond_list[::-1]

