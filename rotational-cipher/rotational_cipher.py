def rotate(text, key):
    edited = []

    for element in text:
        is_upper = element.isupper()
        if element.isalpha():
            ascii_value = ord(element)
            if is_upper:
                shifted_code = (ascii_value - ord('A') + key) % 26 + ord('A')
            else:
                shifted_code = (ascii_value - ord('a') + key) % 26 + ord('a')
            shifted_letter = chr(shifted_code)
            edited.append(shifted_letter)
        else:
            edited.append(element)

    result = "".join(edited)
    return result
