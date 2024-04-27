def sum_of_multiples(limit, multiples):
    return sum(i for i in range(1, limit) if any(i % element == 0 for element in multiples if element != 0))