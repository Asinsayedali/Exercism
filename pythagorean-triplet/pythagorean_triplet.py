def triplets_with_sum(n):
    result = []
    for m in range(1, int(n / 2)):
        for k in range(m + 1, int(n / 2)):
            a = k * k - m * m
            b = 2 * k * m
            c = k * k + m * m
            if a + b + c == n:
                result.append([a, b, c])
    return result

