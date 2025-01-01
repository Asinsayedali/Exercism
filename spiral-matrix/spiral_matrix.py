def spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]

    top, bottom, left, right = 0, size - 1, 0, size - 1

    num = 1
    while num <= size * size:
        for col in range(top, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
    return matrix
