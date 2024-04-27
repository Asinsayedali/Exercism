def is_paired(input_string):
    brackets = ['(', ')', '{', '}', '[', ']']
    new_string = ""
    for element in input_string:
        if element in brackets:
            new_string += element

    brackets_new = ['()', '{}', '[]']
    while any(x in new_string for x in brackets_new):
        for bracket in brackets_new:
            new_string = new_string.replace(bracket, "")
    if new_string == "":
        return True
    else:
        return False
