def is_valid(isbn):
    # Remove hyphens and convert to uppercase for case-insensitivity
    cleaned_isbn = isbn.replace("-", "").upper()


    if len(cleaned_isbn) != 10:
        return False


    if cleaned_isbn.count("X") == 1 and cleaned_isbn[:-1].isdigit():
        # Calculate check digit considering 'X' as 10
        s = sum(int(digit) * (i + 1) for i, digit in enumerate(cleaned_isbn[:-1]))
        check_digit = s % 11
        return check_digit == 10
    elif cleaned_isbn.isdigit():

        s = sum(int(digit) * (i + 1) for i, digit in enumerate(cleaned_isbn))
        check_digit = s % 11
        return check_digit == 0
    else:
        return False




