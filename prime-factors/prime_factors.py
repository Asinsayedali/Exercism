def factors(value):
    factor_value = 2
    result = []
    while value > 1:
        if value % factor_value == 0:
            result.append(factor_value)
            value /= factor_value
        else:
            factor_value += 1
    return result

