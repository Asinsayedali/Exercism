def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        count = 0
        for i in range(0, len(strand_a)):
            if strand_a[i] != strand_b[i]:
                count += 1
                continue
    return count
