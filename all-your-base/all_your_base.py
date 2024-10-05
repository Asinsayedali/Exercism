def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= d < input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if all(d <= 0 for d in digits):
        return [0]

    number = 0
    for d in digits:
        number = number * input_base + d

    result = []
    while number > 0:
        number, remainder = divmod(number, output_base)
        result.append(remainder)
    result.reverse()
    return result
