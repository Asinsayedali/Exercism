def flatten(iterable):
    flattened_list = []
    for element in iterable:
        if isinstance(element, list):
            flattened_list.extend(flatten(element))
        else:
            if element is not None:
                flattened_list.append(element)
    return flattened_list
