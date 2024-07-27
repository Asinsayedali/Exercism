import math


def triplets_with_sum(number):
    N_to_float = float(number)
    res_triplets = []
    for c in range(int(N_to_float / 2) - 1, int((math.sqrt(2) - 1) * N_to_float), -1):
        D = math.sqrt(c ** 2 - N_to_float ** 2 + 2 * N_to_float * c)
        if D == int(D):
            res_triplets.append([int((N_to_float - c - D) / 2), int((N_to_float - c + D) / 2), c])
    return res_triplets
