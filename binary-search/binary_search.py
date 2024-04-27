def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")
    left = 0
    right = len(search_list)-1
    while left <= right:
        middle = (left+right)//2
        if value < search_list[middle]:
            right = middle - 1
        elif value > search_list[middle]:
            left = middle + 1
        else:
            return middle


